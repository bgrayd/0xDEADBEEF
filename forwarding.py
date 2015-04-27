
#Forwarding Unit


def ForwardUnit(EX_MEM, ID_EX, MEM_WB):
	ForwardA = 0
	ForwardB = 0
	
	if (ID_EX.EX.ALUSrc.output == 1):
		rx = ID_EX.rs.output 
	else:
		rx = ID_EX.rd.output
		
		
	if(((MEM_WB.WB.RegWrite.output) ==1) and MEM_WB.regWriteAddr.output != 0):
		if (MEM_WB.regWriteAddr.output == ID_EX.rt.output):
			ForwardB = 2
		
		if (MEM_WB.regWriteAddr.output == rx):
			ForwardA = 2
			
	if (((EX_MEM.WB.RegWrite.output) == 1) and EX_MEM.regWriteAddr.output != 0):
		if (EX_MEM.regWriteAddr.output == rx):
			ForwardA = 1
			
		if (EX_MEM.regWriteAddr.output == ID_EX.rt.output):
			ForwardB = 1
			
	
	return (ForwardA, ForwardB)