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
		
	#send the raising clock edge to each register
	def clkRaiseEdge(self):
		self.PC.clkRaiseEdge()
		self.Instruction.clkRaiseEdge()
		
	def printReg(self):
		print("IF/ID registers:\n\tPC: "+str(self.PC))
		print("\tInstruction: "+str(self.Instruction))
		
	def __str__(self):
		return ("PC: "+str(self.PC)+", Instruction: "+str(self.Instruction))