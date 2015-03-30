from register.py import *
from instrFetchDecodeReg.py import *
from instrDecodeExeReg.py import *
from exeMemReg.py import *
from memWBReg.py import *

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
		(0,0,0,0,0,0,0,0,0):0b0000,	#nop
		(0,0,0,0,0,0,0,1,0):0b0001,	#add
		(0,0,0,1,0,0,0,1,0):0b0010,	#sub
		(0,0,0,2,0,0,0,1,0):0b0011,	#or
		(0,0,0,3,0,0,0,1,0):0b0100,	#xor
		(0,0,0,4,0,0,0,1,0):0b0101,	#and
		(0,0,0,5,0,0,0,1,0):0b0110,	#slt
		(0,0,1,0,1,0,0,1,0):0b1000,	#addi
		(0,1,1,1,0,0,0,0,0):0b1001,	#bne
		(0,1,1,1,0,0,0,0,0):0b1010,	#beq
		(0,0,1,6,1,0,0,1,0):0b1011,	#sll
		(0,0,1,7,1,0,0,1,0):0b1100,	#srl
		(0,0,1,0,1,0,1,0,0):0b1101,	#sw
		(0,0,1,0,1,1,0,1,1):0b1110, #lw
		(1,0,1,0,0,0,0,0,0):0b1111,	#j
		}
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
		IF_ID.Instruction.input = a_instrcMem[PC]
		
		#############################################
		#This is the part of the Write Back Stage
		# it cheats and gets to go early
		#############################################
		if(MEM_WB.WB.RegWrite.output == 1):
			Registers[MEM_WB.regWriteAddr.output] = mux(MEM_WB.WB.MemtoReg.output, MEM_WB.readData.output, MEM_WB.ALUResult.output)
		
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
		
		branchAddr = (IF_ID.PC.output & 0xfff0) | (rd & 0x000f)
		jumpAddr = (((rs<<8) &0x0f00)|((rt<<4)&0x00f0)|(rd&0x000f))
		
		ID_EX.rs.input = rs
		ID_EX.rt.input = rt
		ID_EX.rd.input = rd
		
		#############################################
		#This is the Execute Stage
		#############################################
		
		
		#############################################
		#This is the Memory Stage
		#############################################
		
		
		#############################################
		#This is the Write Back Stage
		#############################################
		
		
		
		PC.clkRaiseEdge()
		IF_ID.clkRaiseEdge()
		ID_EX.clkRaiseEdge()
		EX_MEM .clkRaiseEdge()
		MEM_WB.clkRaiseEdge()