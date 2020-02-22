control_messages = {
    0: {"topic": "CPU.Halt", "label": "HLT"},
    1: {"topic": "CPU.MarIn", "label": "MI"},
    2: {"topic": "CPU.MemIn", "label": "RI"},
    3: {"topic": "CPU.MemOut", "label": "RO"},
    4: {"topic": "CPU.IrIn", "label": "II"},
    5: {"topic": "CPU.IrOut", "label": "IO"},
    6: {"topic": "CPU.ARegIn", "label": "AI"},
    7: {"topic": "CPU.ARegOut", "label": "AO"},
    8: {"topic": "CPU.BRegIn", "label": "BI"},
    9: {"topic": "CPU.BRegOut", "label": "BO"},
    10: {"topic": "CPU.CRegIn", "label": "CI"},
    11: {"topic": "CPU.CRegOut", "label": "CO"},

    12: {"topic": "CPU.AluOut", "label": "EO"},
    13: {"topic": "CPU.AluSub", "label": "SU"},
    14: {"topic": "CPU.TempIn", "label": "TI"},
    15: {"topic": "CPU.OutputWrite", "label": "OI"},

    16: {"topic": "CPU.PcOut", "label": "CO"},
    17: {"topic": "CPU.PcInc", "label": "CE"},
    18: {"topic": "CPU.PcJump", "label": "CJ"},
    19: {"topic": "CPU.FlagIn", "label": "FI"},
    20: {"topic": "CPU.RingReset", "label": "RCR"},
}

decode_messages = {
    "CPU.Halt": "HLT ",
    "CPU.MarIn": "MI ",
    "CPU.MemIn": "RI ",
    "CPU.MemOut": "RO ",
    "CPU.IrIn": "II ",
    "CPU.IrOut": "IO ",
    "CPU.ARegIn": "AI ",
    "CPU.ARegOut": "AO ",
    "CPU.BRegIn": "BI",
    "CPU.BRegOut": "BO",
    "CPU.CRegIn": "CI",
    "CPU.CRegOut": "CO",
    "CPU.AluOut": "EO ",
    "CPU.AluSub": "SU ",
    "CPU.TempIn": "TI ",
    "CPU.OutputWrite": "OI ",
    "CPU.PcOut": "CO ",
    "CPU.PcInc": "CE ",
    "CPU.PcJump": "CJ ",
    "CPU.FlagIn": "FI ",
    "CPU.RingReset": "RCR "
}

operators = {
    0x00: {"operator": "NOP", "op_code": 0x00, "operand1": None, "operand2": None, "addressing": "Non",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xD3: {"operator": "OUT", "op_code": 0xD3, "operand1": "N", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x04: {"operator": "INR B", "op_code": 0x04, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x05: {"operator": "DCR B", "op_code": 0x05, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x06: {"operator": "MVI B", "op_code": 0x06, "operand1": "B", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x0C: {"operator": "INR C", "op_code": 0x0C, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x0D: {"operator": "DCR C", "op_code": 0x0D, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x0E: {"operator": "MVI C", "op_code": 0x0E, "operand1": "C", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x17: {"operator": "RAL", "op_code": 0x17, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x1F: {"operator": "RAR", "op_code": 0x1F, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x2F: {"operator": "CMA", "op_code": 0x2F, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x32: {"operator": "STA", "op_code": 0x32, "operand1": "M", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x3A: {"operator": "LDA", "op_code": 0x3A, "operand1": "M", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x3C: {"operator": "INR A", "op_code": 0x3C, "operand1": "A", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x3D: {"operator": "DCR A", "op_code": 0x3D, "operand1": "A", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x3E: {"operator": "MVI A", "op_code": 0x3E, "operand1": "A", "operand2": "N", "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x41: {"operator": "MOV B,C", "op_code": 0x41, "operand1": "B", "operand2": "C", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x47: {"operator": "MOV B,A", "op_code": 0x47, "operand1": "B", "operand2": "A", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x48: {"operator": "MOV C,B", "op_code": 0x48, "operand1": "C", "operand2": "B", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x4F: {"operator": "MOV C,A", "op_code": 0x4F, "operand1": "C", "operand2": "A", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x76: {"operator": "HLT", "op_code": 0x76, "operand1": None, "operand2": None, "addressing": "Non",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x78: {"operator": "MOV A,B", "op_code": 0x78, "operand1": "A", "operand2": "B", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x79: {"operator": "MOV A,C", "op_code": 0x79, "operand1": "A", "operand2": "C", "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x80: {"operator": "ADD B", "op_code": 0x80, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x81: {"operator": "ADD C", "op_code": 0x81, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0x90: {"operator": "SUB B", "op_code": 0x90, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0x91: {"operator": "SUB C", "op_code": 0x91, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xA0: {"operator": "ANA B", "op_code": 0xA0, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xA1: {"operator": "ANA C", "op_code": 0xA1, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xA8: {"operator": "XRA B", "op_code": 0xA8, "operand1": None, "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xA9: {"operator": "XRA C", "op_code": 0xA9, "operand1": None, "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xB0: {"operator": "ORA B", "op_code": 0xB0, "operand1": "B", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xB1: {"operator": "ORA C", "op_code": 0xB1, "operand1": "C", "operand2": None, "addressing": "Reg",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xC2: {"operator": "JNZ", "op_code": 0xC2, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xC3: {"operator": "JMP", "op_code": 0xC3, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xC9: {"operator": "RET", "op_code": 0xC9, "operand1": None, "operand2": None, "addressing": "Imp",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xCA: {"operator": "JZ", "op_code": 0xCA, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xCD: {"operator": "CALL", "op_code": 0xCD, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xDB: {"operator": "IN", "op_code": 0xDB, "operand1": "N", "operand2": None, "addressing": "Dir",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xE6: {"operator": "ANI", "op_code": 0xE6, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xEE: {"operator": "XRI", "op_code": 0xEE, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},

    0xF6: {"operator": "ORI", "op_code": 0xF6, "operand1": "N", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
    0xFA: {"operator": "JM", "op_code": 0xFA, "operand1": "M", "operand2": None, "addressing": "Imm",
           "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                         ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                         ['CPU.RingReset']]},
}

old_operators = {0: {"operator": "NOP", "op_code": 0, "operand": None,
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.RingReset']]},
                 1: {"operator": "LDA <A>", "op_code": 1, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.ARegIn'],
                                   ['CPU.RingReset']]},
                 2: {"operator": "ADD <A>", "op_code": 2, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.TempIn'],
                                   ['CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                                   ['CPU.RingReset']]},
                 3: {"operator": "SUB <A>", "op_code": 3, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.TempIn'],
                                   ['CPU.AluSub', 'CPU.FlagIn', 'CPU.AluOut', 'CPU.ARegIn'],
                                   ['CPU.RingReset']]},
                 4: {"operator": "STA <A>", "op_code": 4, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.MarIn'],
                                   ['CPU.ARegOut', 'CPU.MemIn'],
                                   ['CPU.RingReset']]},
                 5: {"operator": "LDI", "op_code": 5, "operand": "N",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.ARegIn'],
                                   ['CPU.RingReset']]},
                 6: {"operator": "JMP <A>", "op_code": 6, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.IrOut', 'CPU.PcJump'],
                                   ['CPU.RingReset']]},
                 7: {"operator": "JC <A>", "op_code": 7, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.RingReset']]},
                 8: {"operator": "JZ <A>", "op_code": 8, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.RingReset']]},
                 9: {"operator": "JNZ <A>", "op_code": 9, "operand": "M",
                     "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                   ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                   ['CPU.RingReset']]},
                 10: {"operator": "JM <A>", "op_code": 10, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.RingReset']]},
                 11: {"operator": "NOP", "op_code": 11, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.RingReset']]},
                 12: {"operator": "NOP", "op_code": 12, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.RingReset']]},
                 13: {"operator": "NOP", "op_code": 13, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.RingReset']]},
                 14: {"operator": "OUT", "op_code": 14, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.ARegOut', 'CPU.OutputWrite'],
                                    ['CPU.RingReset']]},
                 15: {"operator": "HLT", "op_code": 15, "operand": None,
                      "microcode": [['CPU.PcOut', 'CPU.MarIn'],
                                    ['CPU.MemOut', 'CPU.IrIn', 'CPU.PcInc'],
                                    ['CPU.Halt'],
                                    ['CPU.RingReset']]}
                 }


class MicroCode:
    def __init__(self):
        self.current_operator = operators[0]
        self.current_microcode = self.current_operator["microcode"]

    def decode_op_code(self, op_code, carry_flag=False, zero_flag=False, negative_flag=False):
        self.current_operator = operators[op_code]
        self.current_microcode = self.current_operator["microcode"]

        if op_code == 7 and carry_flag:
            self.current_microcode = operators[6]["microcode"]

        if op_code == 8 and zero_flag:
            self.current_microcode = operators[6]["microcode"]

        if op_code == 9 and zero_flag:
            self.current_microcode = operators[6]["microcode"]

        if op_code == 10 and negative_flag:
            self.current_microcode = operators[6]["microcode"]

    def get_current_operator(self):
        return self.current_operator

    def get_current_microcode(self):
        return self.current_microcode
