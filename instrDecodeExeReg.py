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
		
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.EX.hold(self._hold)
		self.Mem.hold(self._hold)
		self.WB.hold(self._hold) 
		
		self.PC.hold(self._hold)		#we might be able to remove the PC
		self.regData1.hold(self._hold)
		self.regData2.hold(self._hold)
		self.rs.hold(self._hold)
		self.rt.hold(self._hold)
		self.rd.hold(self._hold)		#rd is also the immediate
		
		self.EX.flush(self._flush)
		self.Mem.flush(self._flush)
		self.WB.flush(self._flush) 
		
		self.PC.flush(self._flush)		#we might be able to remove the PC
		self.regData1.flush(self._flush)
		self.regData2.flush(self._flush)
		self.rs.flush(self._flush)
		self.rt.flush(self._flush)
		self.rd.flush(self._flush)		#rd is also the immediate
		
		self.EX.clkRaiseEdge()
		self.Mem.clkRaiseEdge()
		self.WB.clkRaiseEdge() 
		
		self.PC.clkRaiseEdge()		#we might be able to remove the PC
		self.regData1.clkRaiseEdge()
		self.regData2.clkRaiseEdge()
		self.rs.clkRaiseEdge()
		self.rt.clkRaiseEdge()
		self.rd.clkRaiseEdge()		#rd is also the immediate
		

		self._flush = 0
		self._hold = 0
		
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