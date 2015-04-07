from register import *

################################################
#Class that simulates the registers between the
# Instruction Fetch and the Instruction Decode
# pipeline stages
################################################
class memWBReg:
	def __init__(self):
		self.WB = wbControlReg()
		
		self.readData = register()
		self.ALUResult = register()
		self.regWriteAddr = register()
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.WB.clkRaiseEdge()
		
		self.readData.clkRaiseEdge()
		self.ALUResult.clkRaiseEdge()
		self.regWriteAddr.clkRaiseEdge()
	
	def printReg(self):
		print("Mem/WB Registers:")
		self.WB.printReg()
		print("\tData Memory Read: "+str(self.readData))
		print("\tALU Result: "+str(self.ALUResult))
		print("\tReg Write Addr: "+str(self.regWriteAddr))
		
	def __str__(self):
		return str("WB ctrlReg: "+str(self.WB)+", Data Memory Read: "+str(self.readData)+", ALU Result: "+str(self.ALUResult)+", Reg Write Addr: "+str(self.regWriteAddr))