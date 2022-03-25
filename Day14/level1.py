from dataclasses import dataclass


@dataclass
class DockingModule:
    mask: str
    memory: dict

    def apply_mask(self, memory_address, number_to_add):
        binary_number_to_add = format(number_to_add, "b").zfill(36)
        for idx, bit in enumerate(self.mask):
            if bit.lower() != "x":
                binary_number_to_add = binary_number_to_add[:idx] + bit + binary_number_to_add[idx + 1:]
        self.memory[memory_address] = int(binary_number_to_add, 2)


def main():
    docking_module = DockingModule("", dict())
    with open("input.txt") as f:
        for line in f:
            tokens = line.strip().split('=')
            if tokens[0].strip() == 'mask':
                docking_module.mask = tokens[1].strip()
            else:
                address = tokens[0].strip().split('[')[1].split(']')[0]
                value = int(tokens[1].strip())
                docking_module.apply_mask(address, value)
    print(sum(docking_module.memory.values()))


main()
