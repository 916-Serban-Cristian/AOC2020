from dataclasses import dataclass


@dataclass
class DockingModule:
    mask: str
    memory: dict

    def generate_addresses(self, address, value_to_add):
        x_pos = address.find('X')
        if x_pos == -1:
            self.memory[int(address, 2)] = value_to_add
            return
        address = address[:x_pos] + '1' + address[x_pos + 1:]
        self.generate_addresses(address, value_to_add)
        address = address[:x_pos] + '0' + address[x_pos + 1:]
        self.generate_addresses(address, value_to_add)

    def apply_mask(self, memory_address, number_to_add):
        binary_address = format(memory_address, "b").zfill(36)
        for idx, bit in enumerate(self.mask):
            if bit != '0':
                binary_address = binary_address[:idx] + bit + binary_address[idx + 1:]
        self.generate_addresses(binary_address, number_to_add)


def main():
    docking_module = DockingModule("", dict())
    with open("input.txt") as f:
        for line in f:
            tokens = line.strip().split('=')
            if tokens[0].strip() == 'mask':
                docking_module.mask = tokens[1].strip()
            else:
                address = int(tokens[0].strip().split('[')[1].split(']')[0])
                value = int(tokens[1].strip())
                docking_module.apply_mask(address, value)
    print(sum(docking_module.memory.values()))


main()
