
#Forwarding Unit


def ForwardUnit(rd, rs, rt, MemWrite, RegWrite)
	ForwardA = 00
	ForwardB = 00
	if (exeMemReg.RegWrite and exeMemReg.RegisterRd != 0)
		if (exeMemReg.RegisterRd = instrDecodeExeReg.Register.Rs)
			ForwardA = 10
			
		if (exeMemReg.RegisterRd = instrDecodeExeReg.RegisterRt)
			ForwardB = 10
		
	if(memWBReg.RegWrite and memWBReg.RegisterRd != 0)
		if (memWBReg.RegisterRd = instrDecodeExeReg.RegisterRt)
			ForwardB = 01
		
		if (memWBReg.RegisterRd = instrDecodeExeReg.RegisterRs)
			ForwardA = 01
	
	return (ForwardA, ForwardB)