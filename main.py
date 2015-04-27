from register import *
from instrFetchInstrDecodeReg import *
from instrDecodeExeReg import *
from exeMemReg import *
from memWBReg import *

from memAccess import *
from forwarding import *

import time

def hazard(rt, rs, branch, memRead, regWrite, rsEX):
        if branch == 1:
                if ((regWrite == 1) and (rsEX == 1) and (rsEX == rs)) or (rsEX == rt):
                        return 1
                if ((memRead == 1) and (rt == rs)):
                        return 1
        return 0

def alu(aluop, aluA, aluB):
	if aluop == 0:          #Add
		value = aluA + aluB
	elif aluop == 1:     #Sub
		value = aluA - aluB
	elif aluop == 2:     #Or
		value = aluA | aluB
	elif aluop == 3:     #XOR
		value = aluA ^ aluB
	elif aluop == 4:     #And
		value = aluA & aluB
	elif aluop == 5:     #<
		if aluA < aluB:
			value = 1
		else:
			value = 0
	elif aluop == 6:     #<<
		value = aluA << aluB
	elif aluop == 7:     #>>
		value = aluA >> aluB
	# print("ALUOp:"+str(aluop)+" ALUa:"+str(aluA)+" ALUb:"+str(aluB)+" value:"+str(value))
	return value

def mux(controlSignal, *inputs):
	return inputs[controlSignal]

def splitInst(inst):
	opcode = (inst >> 12 ) & 0xf
	rs = (inst >> 8) & 0xf
	rt = (inst >> 4) & 0xf
	rd = inst & 0xf
	return (opcode, rs, rt, rd)
	
def control(opcode):
	# Jump 0 = false, 1 = true
	# Branch 0 = false, 1 = true
	# RegDst 0 = writeReg:rs
	# ALUOp
	# ALUSrc
	# MemRead
	# MemWrite
	# RegWrite
	# MemtoReg
	Instructions = {
		0b0000:(0,0,0,0,0,0,0,0,0),	#nop
		0b0001:(0,0,0,0,0,0,0,1,0),	#add
		0b0010:(0,0,0,1,0,0,0,1,0),	#sub
		0b0011:(0,0,0,2,0,0,0,1,0),	#or
		0b0100:(0,0,0,3,0,0,0,1,0),	#xor
		0b0101:(0,0,0,4,0,0,0,1,0),	#and
		0b0110:(0,0,0,5,0,0,0,1,0),	#slt
		0b1000:(0,0,1,0,1,0,0,1,0),	#addi
		0b1001:(0,1,1,1,0,0,0,0,0),	#bne
		0b1010:(0,1,1,1,0,0,0,0,0),	#beq
		0b1011:(0,0,1,6,1,0,0,1,0),	#sll
		0b1100:(0,0,1,7,1,0,0,1,0),	#srl
		0b1101:(0,0,1,0,1,0,1,0,0),	#sw
		0b1110:(0,0,1,0,1,1,0,1,1), #lw
		0b1111:(1,0,1,0,0,0,0,0,0),	#j
		}
	# print(str(opcode)+":"+str(Instructions[opcode]))
	return Instructions[opcode]
	
	
def simulateProcessor(a_instrcMem, a_dataMem):
	#initialize Control signals that aren't buffered
	PCSrc = 0
	
	#initialize registers
	PC = register()
	IF_ID = instrFetchInstrDecodeReg()
	ID_EX = instrDecodeExeReg()
	EX_MEM = exeMemReg()
	MEM_WB = memWBReg()
	Registers = [0]*16		#There are 16 different registers
	
	while(1):
		#############################################
		#This is the Instruction Fetch Stage
		#############################################
		IF_ID.PC.input = PC.output+1
		IF_ID.Instruction.input = a_instrcMem[int(PC.output)]
		
		#############################################
		#This is the part of the Write Back Stage
		# it cheats and gets to go early
		#############################################
		if(MEM_WB.WB.RegWrite.output == 1):
			Registers[int(MEM_WB.regWriteAddr.output)] = mux(int(MEM_WB.WB.MemtoReg.output), MEM_WB.ALUResult.output, MEM_WB.readData.output)
			# print(str(int(MEM_WB.regWriteAddr.output))+" : "+str(mux(int(MEM_WB.WB.MemtoReg.output), MEM_WB.ALUResult.output, MEM_WB.readData.output)))
		
		#############################################
		#This is the Instruction Decode Stage
		#############################################
		(opcode, rs, rt, rd) = splitInst(IF_ID.Instruction.output)
		
		(jump, branch, regDst, ID_EX.EX.ALUOp.input, ID_EX.EX.ALUSrc.input, ID_EX.Mem.MemRead.input, ID_EX.Mem.MemWrite.input, ID_EX.WB.RegWrite.input, ID_EX.WB.MemtoReg.input) = control(opcode)
		#read reg 1 is rt
		#read reg 2 is a mux between rs and rd
		#write reg is always rs
		readData1 = Registers[rt]
		readData2 = Registers[mux(regDst, rd, rs)]
		
		branch = ((opcode&0x1)^(readData1 == readData2)) & branch
		branchAddr = (IF_ID.PC.output & 0xffff) + (rd & 0x000f)
		jumpAddr = (((rs<<8) &0x0f00)|((rt<<4)&0x00f0)|(rd&0x000f))
		newAddr = mux(jump, branchAddr, jumpAddr)
		hazardDetected = hazard(ID_EX.rt.output, ID_EX.rs.output, branch, ID_EX.Mem.MemRead.output, EX_MEM.WB.RegWrite.output, EX_MEM.regWriteAddr.output)
		PC.hold(hazardDetected)
		IF_ID.hold(hazardDetected)
		ID_EX.flush(hazardDetected)
		
		ID_EX.rs.input = rs
		ID_EX.rt.input = rt
		ID_EX.rd.input = rd
		ID_EX.regData1.input = readData1
		ID_EX.regData2.input = readData2
		
		#############################################
		#This is the part of the Instruction Fetch Stage
		# it is now so that it can do branching and jumping
		#############################################
		PC.input = mux(branch|jump, IF_ID.PC.input, newAddr)		

		
		#############################################
		#This is the Execute Stage
		#############################################
		(forwarda, forwardb) = ForwardUnit(EX_MEM, ID_EX, MEM_WB)
		EX_MEM.ALUResult.input = alu(ID_EX.EX.ALUOp.output, mux(forwarda, ID_EX.regData1.output, EX_MEM.ALUResult.output, mux(int(MEM_WB.WB.MemtoReg.output), MEM_WB.ALUResult.output, MEM_WB.readData.output)), mux(ID_EX.EX.ALUSrc.output, mux(forwardb, ID_EX.regData2.output, EX_MEM.ALUResult.output, mux(int(MEM_WB.WB.MemtoReg.output), MEM_WB.ALUResult.output, MEM_WB.readData.output)), ID_EX.rs.output))
		
		EX_MEM.Mem.MemRead.input = ID_EX.Mem.MemRead.output
		EX_MEM.Mem.MemWrite.input = ID_EX.Mem.MemWrite.output
		EX_MEM.WB.MemtoReg.input = ID_EX.WB.MemtoReg.output
		EX_MEM.WB.RegWrite.input = ID_EX.WB.RegWrite.output
		EX_MEM.regData2.input = ID_EX.regData2.output
		EX_MEM.regWriteAddr.input = ID_EX.rs.output		
		
		
		#############################################
		#This is the Memory Stage
		#############################################
		MEM_WB.readData.input = MemAccess(EX_MEM.Mem.MemWrite.output, EX_MEM.Mem.MemRead.output, EX_MEM.ALUResult.output, EX_MEM.regData2.output, a_dataMem)
		
		MEM_WB.WB.MemtoReg.input = EX_MEM.WB.MemtoReg.output
		MEM_WB.WB.RegWrite.input = EX_MEM.WB.RegWrite.output
		MEM_WB.regWriteAddr.input = EX_MEM.regWriteAddr.output
		MEM_WB.ALUResult.input = EX_MEM.ALUResult.output
		MEM_WB.regWriteAddr.input = EX_MEM.regWriteAddr.output
		
		#############################################
		#This is the Write Back Stage
		#############################################
		
		
		PC.printReg()
		IF_ID.printReg()
		ID_EX.printReg()
		EX_MEM .printReg()
		MEM_WB.printReg()
		
		PC.clkRaiseEdge()
		IF_ID.clkRaiseEdge()
		ID_EX.clkRaiseEdge()
		EX_MEM .clkRaiseEdge()
		MEM_WB.clkRaiseEdge()
		
		# print(PC.output)
		print(Registers)
		
		time.sleep(1)

a_instrcMem = [0x8104, 0xB114,0x8201, 0xB228, 0x8221, 0xB224, 0x830F, 
	0xB434, 0x8500, 0x8601, 0xB664, 0x8705, 0x6807, 0xA804, 0x0000, 
	0xF02C, 0x0000, 0x8B01, 0x277B, 0xE560, 0x8801, 0xB888, 0x6985, 
	0x990B, 0x0000, 0xC113, 0x3221, 0x8A0F, 0xBAA4, 0x8AAF, 0xBAA8,
	0x0000, 0xDA60, 0xF02A, 0x0000, 0xB332, 0x4443, 0x8A0F, 0xBAA4, 
	0x8AAF, 0x0000,	0xDA60, 0x8662,	0xF00C, 0x0000, 0x0000, 0x0000,
	0x0000, 0x0000]
	
a_dataMem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*10
a_dataMem[16] = 257
a_dataMem[18] = 272
a_dataMem[20] = 17
a_dataMem[22] = 240
a_dataMem[24] = 253

simulateProcessor(a_instrcMem, a_dataMem)
