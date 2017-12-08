# pylint: disable=missing-docstring

class Trampolines:
    @staticmethod
    def jumpsteps1(registers):
        counter = 0
        pc = 0
        while pc >= 0 and pc < len(registers):
            next = pc + registers[pc]
            registers[pc] += 1
            pc = next
            counter += 1

        return counter


if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = [int(x) for x in FILE.read().splitlines()]
    FILE.close()
    print("Trampolines: " , Trampolines.jumpsteps1(INDATA))
