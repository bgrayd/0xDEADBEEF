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
		
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.WB.hold(self._hold)
		
		self.readData.hold(self._hold)
		self.ALUResult.hold(self._hold)
		self.regWriteAddr.hold(self._hold)
		
		self.WB.flush(self._flush)
		
		self.readData.flush(self._flush)
		self.ALUResult.flush(self._flush)
		self.regWriteAddr.flush(self._flush)
		
		self.WB.clkRaiseEdge()
		
		self.readData.clkRaiseEdge()
		self.ALUResult.clkRaiseEdge()
		self.regWriteAddr.clkRaiseEdge()
		
		self._flush = 0
		self._hold = 0
	
	def printReg(self):
		print("Mem/WB Registers:")
		self.WB.printReg()
		print("\tData Memory Read: "+str(self.readData))
		print("\tALU Result: "+str(self.ALUResult))
		print("\tReg Write Addr: "+str(self.regWriteAddr))
		
	def __str__(self):
		return str("WB ctrlReg: "+str(self.WB)+", Data Memory Read: "+str(self.readData)+", ALU Result: "+str(self.ALUResult)+", Reg Write Addr: "+str(self.regWriteAddr))