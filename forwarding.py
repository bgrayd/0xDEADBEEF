
#Forwarding Unit


def ForwardUnit(EX_MEM, ID_EX, MEM_WB)
	ForwardA = 0
	ForwardB = 0
	
	rx = ID_EX.rs.output if ID_EX.EX.ALUSrc else ID_EX.rd.output
	if (EX_MEM.RegWrite.output and EX_MEM.rd.output != 0)
		if (EX_MEM.rd.output = rx)
			ForwardA = 2
			
		if (EX_MEM.rd.output = ID_EX.rt.output)
			ForwardB = 2
		
	if(MEM_WB.RegWrite.output and MEM_WB.rd.output != 0)
		if (MEM_WB.rd.output = ID_EX.rt.output)
			ForwardB = 1
		
		if (MEM_WB.rd.output = rx)
			ForwardA = 1
	
	return (ForwardA, ForwardB)