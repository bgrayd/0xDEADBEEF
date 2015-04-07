################################################
#Class that simulates a raising edge register
#
################################################
class register:
	def __init__(self):
		self.input = 0
		self.output = 0
		
	def __str__(self):
		return (str(self.input)+" -> "+str(self.output))
		
	def clkRaiseEdge(self):
		self.output = self.input
		
		
class exControlReg:
	def __init__(self):
		self.ALUSrc = register()
		self.ALUOp = register()
		
	def clkRaiseEdge(self):
		self.ALUSrc.clkRaiseEdge()
		self.ALUOp.clkRaiseEdge()
		self.RegDst.clkRaiseEdge()
		
	def printReg(self):
		print("Ex control signals: \n\tALUSRC: "+str(self.ALUSrc))
		print("\tALUOp: "+str(self.ALUOp))
		
	def __str__(self):
		return("ALUSRC: "+str(self.ALUSrc)+", ALUOp: "+str(self.ALUOp))
		
		
class memControlReg:
	def __init__(self):
		self.MemWrite = register()
		self.MemRead = register()
		
	def clkRaiseEdge(self):
		self.MemWrite.clkRaiseEdge()
		self.MemRead.clkRaiseEdge()
		
	def printReg(self):
		print("Mem control signals: \n\tMemWrite: "+str(self.MemWrite))
		print("\tMemRead: "+str(self.MemRead))
		
	def __str__(self):
		return ("MemWrite: "+str(self.MemWrite)+", MemRead: "+str(self.MemRead))

		
class wbControlReg:
	def __init__(self):
		self.RegWrite = register()
		self.MemtoReg = register()
		
	def clkRaiseEdge(self):
		self.RegWrite.clkRaiseEdge()
		self.MemtoReg.clkRaiseEdge()
		
	def printReg(self):
		print("WB control signals: \n\tRegWrite: "+str(self.RegWrite))
		print("\tMemtoReg: "+str(self.MemtoReg))
		
	def __str__(self):
		return ("RegWrite: "+str(self.RegWrite)+", MemtoReg: "+str(self.MemtoReg))
		