from register import *

################################################
#Class that simulates the registers between the
# Execution and the Memory pipeline stages
################################################
class exeMemReg:
	def __init__(self):
		self.Mem = memControlReg()
		self.WB = wbControlReg()
		
		self.PCBranch = register()		#This can probably be removed
		self.ALUResult = register()
		self.regData2 = register()
		self.regWriteAddr = register()
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.Mem.clkRaiseEdge()
		self.WB.clkRaiseEdge()
		
		self.PCBranch.clkRaiseEdge()		#This can probably be removed
		self.ALUResult.clkRaiseEdge()
		self.regData2.clkRaiseEdge()
		self.regWriteAddr.clkRaiseEdge()
		
	def printReg(self):
		print("Ex/Mem Registers:")
		self.Mem.printReg()
		self.WB.printReg()
		print("\tPCBranch: "+str(self.PCBranch))
		print("\tALU Result: "+str(self.ALUResult))
		print("\tData Register2: "+str(self.regData2))
		print("\tReg Write Addr: "+str(self.regWriteAddr))
	
	def __str__(self):
		return str("Mem ctrlReg: "+str(self.Mem)+", WB ctrlReg: "+str(self.WB)+", PCBranch: "+str(self.PCBranch)+", ALU Result: "+str(self.ALUResult)+", Data Register2: "+str(self.regData2)+", Reg Write Addr: "+str(self.regWriteAddr))