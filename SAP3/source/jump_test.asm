	.org 0

CPU:	LXI SP,(STACK)	;SET THE STACK POINTER
;INITIALIZE A REG. AND CLEAR ALL FLAGS
	ANI 0
;TEST "JZ"
	JZ (J010)
	CALL (CPUER)
;TEST "JNC"
J010:	JNC (J020)
	CALL CPUER
;TEST "JPE"
J020:	JPE (J030)
	CALL CPUER
;TEST "JP"	
J030:	JP (J040)
	CALL	CPUER
;Test JNZ
J040:	JNZ (J050)
;TEST "JC"
	JC J050
;TEST "JPO"
	JPO (J050)
;TEST "JM"
	JM J050
;TEST "JMP" (IT'S A LITTLE LATE,BUT WHAT THE HELL!
	JMP J060
J050:	CALL CPUER
;Set A=6,C=0,P=1,S=0,Z=0
J060:	ADI 6
;TEST "JNZ"
	JNZ J070
	CALL CPUER
;TEST "JC"
J070:	JC J080
;TEST "JPO"
	JPO J080
;TEST "JP"
	JP J090
J080:	CALL CPUER
;A=76H,C=0,P=0,S=0,Z=0
J090:	ADI	070H	
;TEST "JPO"
	JPO	J100
	CALL	CPUER
J100:	JM	J110
	JZ	J110
	JNC	J120
J110:	CALL	CPUER
;A=F7H,C=0,P=0,S=1,Z=0
J120:	ADI	081H
	JM	J130
	CALL	CPUER
J130:	JZ	J140
	JC	J140
	JPO	J150
J140:	CALL	CPUER
;A=F5H,C=1,P=1,S=1,Z=0
J150:	ADI	0FEH	
	JC	J160
	CALL	CPUER
J160:	JZ	J170
	JPO	J170
	JM	AIMM
J170:	CALL	CPUER
;
;
;
;TEST ACCUMULATOR IMMEDIATE INSTRUCTIONS
;
;A=F5H,C=0,Z=0
AIMM:	CPI	0
	JC	CPIE
	JZ	CPIE
;A=F5H,C=0,Z=1
	CPI	0F5H
	JC	CPIE	
	JNZ	CPIE	
;A=F5H,C=1,Z=0
	CPI	0FFH
	JZ	CPIE	
	JC	ACII	
CPIE:	CALL	CPUER
;A=F5H+0AH+CARRY(1)=0,C=1
ACII:	ACI	00AH
;A=0+0AH+CARRY(0)=0BH,C=0
	ACI	00AH
	CPI	00BH
	JZ	SUII	
	CALL	CPUER
;A=FFH,C=0
SUII:	SUI	00CH
;A=F0H,C=1
	SUI	00FH
	CPI	0F0H
	JZ	SBII
	CALL	CPUER
;A=F0H-0F1H-CARRY(0)=FFH,C=1
SBII:	SBI	0F1H
;A=FFH-OEH-CARRY(1)=F0H,C=0
	SBI	00EH	
	CPI	0F0H
	JZ	ANII
	CALL	CPUER
;A=F0H<AND>55H=50H,C=0,P=1,S=0,Z=0
ANII:	ANI	055H
	CPI	050H
	JZ	ORII
	CALL	CPUER
;A=50H<OR>3AH=7AH,C=0,P=0,S=0,Z=0
ORII:	ORI	03AH
	CPI	07AH
	JZ	XRII
	CALL	CPUER
;A=7AH<XOR>0FH=75H,C=0,P=0,S=0,Z=0
XRII:	XRI	00FH
	CPI	075H
	JZ	MOVI
	CALL	CPUER

;
;TEST "MOV","INR",AND "DCR" INSTRUCTIONS
;
MOVI:	MVI	A,077H
	INR	A
	MOV	B,A
	INR	B
	MOV	C,B
	DCR	C
	MOV	D,C
	MOV	E,D
	MOV	H,E
	MOV	L,H
;TEST "MOV" A,L,H,E,D,C,B,A
	MOV	A,L
	DCR	A
	MOV	C,A
	MOV	E,C
	MOV	L,E
	MOV	B,L
	MOV	D,B
	MOV	H,D
;TEST "MOV" A,H,D,B,L,E,C,A
	MOV	A,H
	MOV	D,A
	INR	D
	MOV	L,D
	MOV	C,L
	INR	C
	MOV	H,C
	MOV	B,H
	DCR	B
	MOV	E,B
;TEST "MOV" A,E,B,H,C,L,D,A
	MOV	A,E
	MOV	E,A
	INR	E
	MOV	B,E
	MOV	H,B
	INR	H
	MOV	C,H
	MOV	L,C
	MOV	D,L
	DCR	D
;TEST "MOV" A,D,L,C,H,B,E,A	
	MOV	A,D
	MOV	H,A
	DCR	H
	MOV	D,H
	MOV	B,D
	MOV	L,B
	INR	L
	MOV	E,L
	DCR	E
	MOV	C,E
;TEST "MOV" A,C,E,L,B,D,H,A
	MOV	A,C
	MOV	L,A
	DCR	L
	MOV	H,L
	MOV	E,H
	MOV	D,E
	MOV	C,D
	MOV	B,C
	MOV	A,B
	CPI	077H
;TEST "MOV" A,B,C,D,E,H,L,A
	JZ	C010
	CALL	CPUER	

;A=0,C=0,P=1,S=0,Z=1
C010:	ANI	000H	
;TEST "CC"
	CC	CPUER	
;TEST "CPO"
	CPO	CPUER	
;TEST "CM"
	CM	CPUER	
;TEST "CNZ"
	CNZ	CPUER	
	CPI	000H
;A=0,C=0,P=0,S=0,Z=1
	JZ	C020	
	CALL	CPUER
C020:	SUI	077H	;A=89H,C=1,P=0,S=1,Z=0
	CNC	CPUER	;TEST "CNC"
	CPE	CPUER	;TEST "CPE"
	CP	CPUER	;TEST "CP"
	CZ	CPUER	;TEST "CZ"
	CPI	089H
	JZ	C030	;TEST FOR "CALLS" TAKING BRANCH
	CALL	CPUER
C030:	ANI	0FFH	;SET FLAGS BACK!
	CPO	CPOI	;TEST "CPO"
	CPI	0D9H
	JZ	GOOD_EXIT	;TEST "CALL" SEQUENCE SUCCESS
	CALL	CPUER
CPOI:	RPE		;TEST "RPE"
	ADI	010H	;A=99H,C=0,P=0,S=1,Z=0
	CPE	CPEI	;TEST "CPE"
	ADI	002H	;A=D9H,C=0,P=0,S=1,Z=0
	RPO		;TEST "RPO"
	CALL	CPUER
CPEI:	RPO		;TEST "RPO"
	ADI	020H	;A=B9H,C=0,P=0,S=1,Z=0
	CM	CMI	;TEST "CM"
	ADI	004H	;A=D7H,C=0,P=1,S=1,Z=0
	RPE		;TEST "RPE"
	CALL	CPUER
CMI:	RP		;TEST "RP"
	ADI	080H	;A=39H,C=1,P=1,S=0,Z=0
	CP	TCPI	;TEST "CP"
	ADI	080H	;A=D3H,C=0,P=0,S=1,Z=0
	RM		;TEST "RM"
	CALL	CPUER
TCPI:	RM		;TEST "RM"
	ADI	040H	;A=79H,C=0,P=0,S=0,Z=0
	CNC	CNCI	;TEST "CNC"
	ADI	040H	;A=53H,C=0,P=1,S=0,Z=0
	RP		;TEST "RP"
	CALL	CPUER
CNCI:	RC		;TEST "RC"
	ADI	08FH	;A=08H,C=1,P=0,S=0,Z=0
	CC	CCI	;TEST "CC"
	SUI	002H	;A=13H,C=0,P=0,S=0,Z=0
	RNC		;TEST "RNC"
	CALL	CPUER
CCI:	RNC		;TEST "RNC"
	ADI	0F7H	;A=FFH,C=0,P=1,S=1,Z=0
	CNZ	CNZI	;TEST "CNZ"
	ADI	0FEH	;A=15H,C=1,P=0,S=0,Z=0
	RC		;TEST "RC"
	CALL	CPUER
;TEST "RZ"
CNZI:	RZ		
;A=00H,C=1,P=1,S=0,Z=1
	ADI	001H	
;TEST "CZ"
	CZ	CZI	
;A=17H,C=1,P=1,S=0,Z=0
	ADI	0D0H	
;TEST "RNZ"
	RNZ		
	CALL	CPUER
;TEST "RNZ"
CZI:	RNZ		
;A=47H,C=0,P=1,S=0,Z=0
	ADI	047H	
;A=47H,C=0,P=1,S=0,Z=1
	CPI	047H	
;TEST "RZ"
	RZ		
	CALL	CPUER
;
GOOD_EXIT:
	MVI A,1
	OUT 3
	HLT

CPUER:	MVI A,255
	OUT 3
	HLT

	.org 512
STACK:	.byte 0

	.end
