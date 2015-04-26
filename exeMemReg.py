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
		
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.Mem.hold(self._hold)
		self.WB.hold(self._hold)
		
		self.PCBranch.hold(self._hold)		#This can probably be removed
		self.ALUResult.hold(self._hold)
		self.regData2.hold(self._hold)
		self.regWriteAddr.hold(self._hold)
		
		self.Mem.flush(self._flush)
		self.WB.flush(self._flush)
		
		self.PCBranch.flush(self._flush)		#This can probably be removed
		self.ALUResult.flush(self._flush)
		self.regData2.flush(self._flush)
		self.regWriteAddr.flush(self._flush)
		
		self.Mem.clkRaiseEdge()
		self.WB.clkRaiseEdge()
		
		self.PCBranch.clkRaiseEdge()		#This can probably be removed
		self.ALUResult.clkRaiseEdge()
		self.regData2.clkRaiseEdge()
		self.regWriteAddr.clkRaiseEdge()
		
		self._flush = 0
		self._hold = 0
		
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