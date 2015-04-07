from register import *

################################################
#Class that simulates the registers between the
# Instruction Decode and the Execution
# pipeline stages
################################################
class instrDecodeExeReg:
	def __init__(self):
		self.EX = exControlReg()
		self.Mem = memControlReg()
		self.WB = wbControlReg()
		
		self.PC = register()		#we might be able to remove the PC
		self.regData1 = register()
		self.regData2 = register()
		self.rs = register()
		self.rt = register()
		self.rd = register()		#rd is also the immediate
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.EX.clkRaiseEdge()
		self.Mem.clkRaiseEdge()
		self.WB.clkRaiseEdge() 
		
		self.PC.clkRaiseEdge()		#we might be able to remove the PC
		self.regData1.clkRaiseEdge()
		self.regData2.clkRaiseEdge()
		self.rs.clkRaiseEdge()
		self.rt.clkRaiseEdge()
		self.rd.clkRaiseEdge()		#rd is also the immediate
		
	def __str__(self):
		return str("EX ctrlReg: "+str(self.EX)+", Mem ctrlReg: "+str(self.Mem)+", WB ctrlReg: "+str(self.WB)+", PC: "+str(self.PC)+", Data Register1: "+str(self.regData1)+", Data Register2: "+str(self.regData2)+", RS: "+str(self.rs)+", RT: "+str(self.rt)+", RD: "+str(self.rd))
		
	def printReg(self):
		print("ID/Ex Registers:")
		self.EX.printReg()
		self.Mem.printReg()
		self.WB.printReg()
		print("\tPC: "+str(self.PC))
		print("\tData Register1: "+str(self.regData1))
		print("\tData Register2: "+str(self.regData2))
		print("\tRS: "+str(self.rs))
		print("\tRT: "+str(self.rt))
		print("\tRD: "+str(self.rd))