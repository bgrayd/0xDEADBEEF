from register.py import *
from instrFetchDecodeReg.py import *
from instrDecodeExeReg.py import *
from exeMemReg.py import *
from memWBReg.py import *

def simulateProcessor(a_instrcMem, a_dataMem):
	PC = register()
	IF_ID = instrFetchInstrDecodeReg()
	ID_EX = instrDecodeExeReg()
	EX_MEM = exeMemReg()
	MEM_WB = memWBReg()
	Registers = [0]*16		#There are 16 different registers
	
	while(1):
		#############################################
		#This is the Instruction Fetch Stage
		#############################################
		
		#############################################
		#This is the Instruction Decode Stage
		#############################################
		
		#############################################
		#This is the Execute Stage
		#############################################
		
		#############################################
		#This is the Memory Stage
		#############################################
		
		#############################################
		#This is the Write Back Stage
		#############################################