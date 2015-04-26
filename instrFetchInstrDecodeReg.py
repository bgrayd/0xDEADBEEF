from register import *

################################################
#Class that simulates the registers between the
# Instruction Fetch and the Instruction Decode
# pipeline stages
################################################
class instrFetchInstrDecodeReg:
	def __init__(self):
		self.PC = register()
		self.Instruction = register()
		self._flush = 0
		self._hold = 0
		
	def hold(self, hold):
		self._hold = hold
		
	def flush(self, flush):
		self._flush = flush
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.PC.hold(self._hold)
		self.Instruction.hold(self._hold)
		
		self.PC.flush(self._flush)
		self.Instruction.flush(self._flush)
		
		self.PC.clkRaiseEdge()
		self.Instruction.clkRaiseEdge()
		
		self._flush = 0
		self._hold = 0
		
	def printReg(self):
		print("IF/ID registers:\n\tPC: "+str(self.PC))
		print("\tInstruction: "+str(self.Instruction))
		
	def __str__(self):
		return ("PC: "+str(self.PC)+", Instruction: "+str(self.Instruction))