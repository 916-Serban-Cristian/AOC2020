from dataclasses import dataclass


@dataclass
class Instruction:
    name: str
    value: int


class GameConsoleException(Exception):
    pass


class GameConsole:
    def __init__(self):
        self.accumulator = 0
        self.instruction_pointer = 0
        self.memory = []

    def load_program_from_text(self):
        with open("input.txt") as f:
            for line in f:
                line = line.split()
                instr_name = line[0]
                instr_value = int(line[1])
                self.memory.append(Instruction(instr_name, instr_value))

    def run_program(self):
        executed_instructions = [0] * len(self.memory)
        while self.instruction_pointer < len(self.memory):
            current_instruction = self.memory[self.instruction_pointer]
            if executed_instructions[self.instruction_pointer] == 1:
                raise GameConsoleException(
                    "Infinite loop detected\nCurrent value of accumulator is {0}\nCurrent instruction pointer is {1}".format(
                        self.accumulator, self.instruction_pointer))
            executed_instructions[self.instruction_pointer] = 1
            if current_instruction.name == "nop":
                self.NOP()
            elif current_instruction.name == "acc":
                self.ACC(current_instruction)
            elif current_instruction.name == "jmp":
                self.JMP(current_instruction)
        return "Program executed successfully. The final value of the accumulator is {0}".format(self.accumulator)

    def NOP(self):
        self.instruction_pointer += 1

    def ACC(self, instruction):
        self.accumulator += instruction.value
        self.instruction_pointer += 1

    def JMP(self, instruction):
        self.instruction_pointer += instruction.value


def run_console():
    console = GameConsole()
    console.load_program_from_text()
    try:
        console.run_program()
    except GameConsoleException as gce:
        print(gce)
