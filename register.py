################################################
#Class that simulates a raising edge register
#
################################################
class register:
	def __init__(self):
		self.input = 0
		self.output = 0
		self._flush = 0
		self._hold = 0
		
	def __str__(self):
		return (str(self.input)+" -> "+str(self.output))
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
	
	def clkRaiseEdge(self):
		if not self._hold:
			self.output = self.input
		if self._flush:
			self.output = 0
		self._flush = 0
		self._hold = 0
		
	def printReg(self):
		print(str(self.input)+" -> "+str(self.output))
		
		
class exControlReg:
	def __init__(self):
		self.ALUSrc = register()
		self.ALUOp = register()
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	def clkRaiseEdge(self):
		self.ALUSrc.hold(self._hold)
		self.ALUOp.hold(self._hold)
		self.ALUSrc.flush(self._flush)
		self.ALUOp.flush(self._flush)
		self.ALUSrc.clkRaiseEdge()
		self.ALUOp.clkRaiseEdge()
		self._flush = 0
		self._hold = 0
		
	def printReg(self):
		print("Ex control signals: \n\tALUSRC: "+str(self.ALUSrc))
		print("\tALUOp: "+str(self.ALUOp))
		
	def __str__(self):
		return("ALUSRC: "+str(self.ALUSrc)+", ALUOp: "+str(self.ALUOp))
		
		
class memControlReg:
	def __init__(self):
		self.MemWrite = register()
		self.MemRead = register()
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	def clkRaiseEdge(self):
		self.MemWrite.hold(self._hold)
		self.MemRead.hold(self._hold)
		self.MemWrite.flush(self._flush)
		self.MemRead.flush(self._flush)
		self.MemWrite.clkRaiseEdge()
		self.MemRead.clkRaiseEdge()
		self._flush = 0
		self._hold = 0
		
	def printReg(self):
		print("Mem control signals: \n\tMemWrite: "+str(self.MemWrite))
		print("\tMemRead: "+str(self.MemRead))
		
	def __str__(self):
		return ("MemWrite: "+str(self.MemWrite)+", MemRead: "+str(self.MemRead))

		
class wbControlReg:
	def __init__(self):
		self.RegWrite = register()
		self.MemtoReg = register()
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	def clkRaiseEdge(self):
		self.RegWrite.hold(self._hold)
		self.MemtoReg.hold(self._hold)
		self.RegWrite.flush(self._flush)
		self.MemtoReg.flush(self._flush)
		self.RegWrite.clkRaiseEdge()
		self.MemtoReg.clkRaiseEdge()
		self._flush = 0
		self._hold = 0
		
	def printReg(self):
		print("WB control signals: \n\tRegWrite: "+str(self.RegWrite))
		print("\tMemtoReg: "+str(self.MemtoReg))
		
	def __str__(self):
		return ("RegWrite: "+str(self.RegWrite)+", MemtoReg: "+str(self.MemtoReg))
		