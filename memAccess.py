# Memory Access Function



def MemAccess(writeEnable, readEnable, readAddress, writeAddress, writeData, a_dataMem)

	if writeEnable == 1:
		a_dataMem[writeAddress] = writeData
		
	if readEnable == 1:
		return a_dataMem[readAddress]
		
		
	
		
		
	
		
	


