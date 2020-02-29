control_messages = [
    {"topic": "CPU.Halt", "label": "HLT"},

    {"topic": "CPU.MarIn", "label": "MI"},
    {"topic": "CPU.MemIn", "label": "RI"},
    {"topic": "CPU.MemOut", "label": "RO"},

    {"topic": "CPU.IrIn", "label": "II"},
    {"topic": "CPU.IrAlIn", "label": "IAL"},
    {"topic": "CPU.IrAhIn", "label": "IAH"},
    {"topic": "CPU.IrOut", "label": "IO"},

    {"topic": "CPU.ARegIn", "label": "AI"},
    {"topic": "CPU.ARegOut", "label": "AO"},
    {"topic": "CPU.BRegIn", "label": "BI"},
    {"topic": "CPU.BRegOut", "label": "BO"},
    {"topic": "CPU.CRegIn", "label": "CI"},
    {"topic": "CPU.CRegOut", "label": "CO"},

    {"topic": "CPU.AluAdd", "label": "ADD"},
    {"topic": "CPU.AluCma", "label": "CMA"},
    {"topic": "CPU.AluDec", "label": "DEC"},
    {"topic": "CPU.AluInc", "label": "INC"},
    {"topic": "CPU.AluLand", "label": "LAND"},
    {"topic": "CPU.AluLda", "label": "LDA"},
    {"topic": "CPU.AluLdb", "label": "LDB"},
    {"topic": "CPU.AluLdc", "label": "LDC"},
    {"topic": "CPU.AluLor", "label": "LOR"},
    {"topic": "CPU.AluLxor", "label": "LXOR"},
    {"topic": "CPU.AluOut", "label": "EO"},
    {"topic": "CPU.AluRar", "label": "RAR"},
    {"topic": "CPU.AluRal", "label": "RAL"},
    {"topic": "CPU.AluSub", "label": "SUB"},

    {"topic": "CPU.TempIn", "label": "TI"},

    {"topic": "CPU.OutputWrite", "label": "OI"},

    {"topic": "CPU.PcOut", "label": "CO"},
    {"topic": "CPU.PcOutLow", "label": "COL"},
    {"topic": "CPU.PcOutHigh", "label": "COH"},
    {"topic": "CPU.PcInc", "label": "C+"},
    {"topic": "CPU.PcJump", "label": "CJ"},

    {"topic": "CPU.SpOut", "label": "SO"},
    {"topic": "CPU.SpIn", "label": "SI"},
    {"topic": "CPU.SpInc", "label": "S+"},
    {"topic": "CPU.SpDec", "label": "S-"},

    {"topic": "CPU.FlagIn", "label": "FI"},

    {"topic": "CPU.RingReset", "label": "RCR"},

    {"topic": "CPU.IllegalInst", "label": "ILL"}
]

decode_messages = {
    "CPU.Halt": "HLT ",
    "CPU.MarIn": "MI ",
    "CPU.MemIn": "RI ",
    "CPU.MemOut": "RO ",
    "CPU.IrIn": "II ",
    "CPU.IrAlIn": "IAL ",
    "CPU.IrAhIn": "IAH ",
    "CPU.IrOut": "IO ",
    "CPU.ARegIn": "AI ",
    "CPU.ARegOut": "AO ",
    "CPU.BRegIn": "BI ",
    "CPU.BRegOut": "BO ",
    "CPU.CRegIn": "CI ",
    "CPU.CRegOut": "CO ",
    "CPU.AluLda": "LDA ",
    "CPU.AluLdb": "LDB ",
    "CPU.AluLdc": "LDC ",
    "CPU.AluLand": "LAND ",
    "CPU.AluLor": "LOR ",
    "CPU.AluLxor": "LXOR ",
    "CPU.AluOut": "EO ",
    "CPU.AluAdd": "ADD ",
    "CPU.AluSub": "SUB ",
    "CPU.AluDec": "DEC ",
    "CPU.AluInc": "INC ",
    "CPU.AluRar": "RAR ",
    "CPU.AluRal": "RAL ",
    "CPU.AluCma": "CMA ",
    "CPU.TempIn": "TI ",
    "CPU.OutputWrite": "OI ",
    "CPU.PcOut": "CO ",
    "CPU.PcOutLow": "COL ",
    "CPU.PcOutHigh": "COH ",
    "CPU.PcInc": "C+ ",
    "CPU.PcJump": "CJ ",
    "CPU.SpIn": "SI ",
    "CPU.SpOut": "SO ",
    "CPU.SpInc": "S+ ",
    "CPU.SpDec": "S- ",
    "CPU.FlagIn": "FI ",
    "CPU.RingReset": "RCR ",
    "CPU.IllegalInst": "ILL "
}

operators = {
    0x00: {"operator": "NOP", "op_code": 0x00, "operand1": None, "operand2": None, "addressing": "Non",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xD3: {"operator": "OUT", "op_code": 0xD3, "operand1": "N", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         # TODO Need output port selection from operand
                         ['CPU.ARegOut', 'CPU.OutputWrite'],
                         ['CPU.RingReset']]},

    0x04: {"operator": "INR B", "op_code": 0x04, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLdb', 'CPU.AluInc', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.BRegIn'],
                         ['CPU.RingReset']]},
    0x05: {"operator": "DCR B", "op_code": 0x05, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLdb', 'CPU.AluInc', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.BRegIn'],
                         ['CPU.RingReset']]},
    0x06: {"operator": "MVI B", "op_code": 0x06, "operand1": "B", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.BRegIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x0C: {"operator": "INR C", "op_code": 0x0C, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLdc', 'CPU.AluInc', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.CRegIn'],
                         ['CPU.RingReset']]},
    0x0D: {"operator": "DCR C", "op_code": 0x0D, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLdc', 'CPU.AluDec', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.CRegIn'],
                         ['CPU.RingReset']]},
    0x0E: {"operator": "MVI C", "op_code": 0x0E, "operand1": "C", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.CRegIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x17: {"operator": "RAL", "op_code": 0x17, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda'],
                         ['CPU.AluRal', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x1F: {"operator": "RAR", "op_code": 0x1F, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda'],
                         ['CPU.AluRar', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0x2F: {"operator": "CMA", "op_code": 0x2F, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda'],
                         ['CPU.AluCma', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0x32: {"operator": "STA", "op_code": 0x32, "operand1": "M", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.IrOut', 'CPU.MarIn'],
                         ['CPU.ARegOut', 'CPU.MemIn'],
                         ['CPU.RingReset']]},

    0x3A: {"operator": "LDA", "op_code": 0x3A, "operand1": "M", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.IrOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0x3C: {"operator": "INR A", "op_code": 0x3C, "operand1": "A", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.AluInc', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x3D: {"operator": "DCR A", "op_code": 0x3D, "operand1": "A", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.AluInc', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x3E: {"operator": "MVI A", "op_code": 0x3E, "operand1": "A", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.ARegIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x41: {"operator": "MOV B,C", "op_code": 0x41, "operand1": "B", "operand2": "C", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.CRegOut', 'CPU.BRegIn'],
                         ['CPU.RingReset']]},
    0x47: {"operator": "MOV B,A", "op_code": 0x47, "operand1": "B", "operand2": "A", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.ARegOut', 'CPU.BRegIn'],
                         ['CPU.RingReset']]},

    0x48: {"operator": "MOV C,B", "op_code": 0x48, "operand1": "C", "operand2": "B", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.BARegOut', 'CPU.CRegIn'],
                         ['CPU.RingReset']]},
    0x4F: {"operator": "MOV C,A", "op_code": 0x4F, "operand1": "C", "operand2": "A", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.ARegOut', 'CPU.CRegIn'],
                         ['CPU.RingReset']]},

    0x76: {"operator": "HLT", "op_code": 0x76, "operand1": None, "operand2": None, "addressing": "Non",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.Halt'],
                         ['CPU.RingReset']]},

    0x78: {"operator": "MOV A,B", "op_code": 0x78, "operand1": "A", "operand2": "B", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.BRegOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x79: {"operator": "MOV A,C", "op_code": 0x79, "operand1": "A", "operand2": "C", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.CRegOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0x80: {"operator": "ADD B", "op_code": 0x80, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.BRegOut', 'CPU.TempIn'],
                         ['CPU.AluAdd', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x81: {"operator": "ADD C", "op_code": 0x81, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.CRegOut', 'CPU.TempIn'],
                         ['CPU.AluAdd', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0x90: {"operator": "SUB B", "op_code": 0x90, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.BRegOut', 'CPU.TempIn'],
                         ['CPU.AluSub', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0x91: {"operator": "SUB C", "op_code": 0x91, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.CRegOut', 'CPU.TempIn'],
                         ['CPU.AluSub', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0xA0: {"operator": "ANA B", "op_code": 0xA0, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.BRegOut', 'CPU.TempIn'],
                         ['CPU.AluLand', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0xA1: {"operator": "ANA C", "op_code": 0xA1, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.CRegOut', 'CPU.TempIn'],
                         ['CPU.AluLand', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0xA8: {"operator": "XRA B", "op_code": 0xA8, "operand1": None, "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.BRegOut', 'CPU.TempIn'],
                         ['CPU.AluLxor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0xA9: {"operator": "XRA C", "op_code": 0xA9, "operand1": None, "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.CRegOut', 'CPU.TempIn'],
                         ['CPU.AluLxor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0xB0: {"operator": "ORA B", "op_code": 0xB0, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.BRegOut', 'CPU.TempIn'],
                         ['CPU.AluLor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0xB1: {"operator": "ORA C", "op_code": 0xB1, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.CRegOut', 'CPU.TempIn'],
                         ['CPU.AluLor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0xC2: {"operator": "JNZ", "op_code": 0xC2, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xC3: {"operator": "JMP", "op_code": 0xC3, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.IrOut', 'CPU.PcJump'],
                         ['CPU.RingReset']]},
    0xC9: {"operator": "RET", "op_code": 0xC9, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.SpOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.SpDec'],
                         ['CPU.SpOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.SpDec'],
                         ['CPU.IrOut', 'CPU.PcJump'],
                         ['CPU.RingReset']]},
    0xCA: {"operator": "JZ", "op_code": 0xCA, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xCD: {"operator": "CALL", "op_code": 0xCD, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc', 'CPU.SpInc'],
                         ['CPU.SpOut', 'CPU.MarIn'],
                         ['CPU.PcOutLow', 'CPU.MemIn', 'CPU.SpInc'],
                         ['CPU.SpOut', 'CPU.MarIn'],
                         ['CPU.PcOutHigh', 'CPU.MemIn'],
                         ['CPU.IrOut', 'CPU.PcJump'],
                         ['CPU.RingReset']]},

    0xDA: {"operator": "JC", "op_code": 0xDA, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xDB: {"operator": "IN", "op_code": 0xDB, "operand1": "N", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         # Need input port select
                         ['CPU.RingReset']]},

    0xE6: {"operator": "ANI", "op_code": 0xE6, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.IrOut', 'CPU.TempIn'],
                         ['CPU.AluLand', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0xEE: {"operator": "XRI", "op_code": 0xEE, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.IrOut', 'CPU.TempIn'],
                         ['CPU.AluLxor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},
    0xF6: {"operator": "ORI", "op_code": 0xF6, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.AluLda', 'CPU.IrOut', 'CPU.TempIn'],
                         ['CPU.AluLor', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                         ['CPU.RingReset']]},

    0xFA: {"operator": "JM", "op_code": 0xFA, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAlIn', 'CPU.PcInc'],
                         ['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrAhIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
}

invalid_operator = {"operator": "***", "op_code": 0x00, "operand1": None, "operand2": None, "addressing": "Non",
                    "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                  ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                  ['CPU.IllegalInst', 'CPU.Halt'],
                                  ['CPU.RingReset']]}


class MicroCode:
    def __init__(self):
        self.current_operator = operators[0]
        self.current_microcode = self.current_operator["microcode"]

    def decode_op_code(self, op_code, carry_flag=False, zero_flag=False, negative_flag=False):
        if op_code in operators:
            self.current_operator = operators[op_code]
            self.current_microcode = self.current_operator["microcode"]

            # JC - If this is the Jump if Carry and carry flag is set Just use the Jump Microcode
            if op_code == 0xFB and carry_flag:
                self.current_microcode = operators[0xC3]["microcode"]

            # JNZ - If this is the Jump if Not Zero and zero flag is clear Just use the Jump Microcode
            if op_code == 0xC2 and not zero_flag:
                self.current_microcode = operators[0xC3]["microcode"]

            # JZ - If this is the Jump if Zero and zero flag is set Just use the Jump Microcode
            if op_code == 0xCA and zero_flag:
                self.current_microcode = operators[0xC3]["microcode"]

            # JM - If this is the Jump if minus and negative flag is set Just use the Jump Microcode
            if op_code == 0xFA and negative_flag:
                self.current_microcode = operators[0xC3]["microcode"]
        else:
            self.current_operator = invalid_operator
            self.current_microcode = self.current_operator["microcode"]

    def get_current_operator(self):
        return self.current_operator

    def get_current_microcode(self):
        return self.current_microcode
