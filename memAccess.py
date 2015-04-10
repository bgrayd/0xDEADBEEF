# Memory Access Function



def MemAccess(writeEnable, readEnable, address, writeData, a_dataMem):
	if writeEnable == 1:
		a_dataMem[address] = writeData
		
	if readEnable == 1:
		return a_dataMem[address]
		
		
	
		
		
	
		
	


