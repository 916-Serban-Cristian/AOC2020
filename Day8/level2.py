import copy

from level1 import GameConsole, GameConsoleException


def run_console():
    console = GameConsole()
    console.load_program_from_text()
    fixed = False
    change_history = []
    while not fixed:
        memory_copy = copy.deepcopy(console.memory)
        for address, instruction in enumerate(console.memory):
            if address not in change_history:
                if instruction.name == "jmp":
                    instruction.name = "nop"
                    change_history.append(address)
                    break
                elif instruction.name == "nop":
                    instruction.name = "jmp"
                    change_history.append(address)
                    break
        try:
            print(console.run_program())
            fixed = True
        except GameConsoleException:
            console.memory = memory_copy
            console.instruction_pointer = 0
            console.accumulator = 0


run_console()
