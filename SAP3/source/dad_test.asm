	.org 0
	LXI	SP,STACK
	LXI	BC,15
	LXI	DE,240
	MVI	H,010H
	MVI	L,020H
	DAD	BC
	DAD	DE
	DAD	HL
	DAD	SP
	HLT


	.org 240
STACK:	.byte	0

	.end