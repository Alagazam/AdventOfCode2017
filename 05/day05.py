# pylint: disable=missing-docstring
import copy

class Trampolines:
    @staticmethod
    def jumpsteps1(registers):
        counter = 0
        index = 0
        while index >= 0 and index < len(registers):
            nextindex = index + registers[index]
            registers[index] += 1
            index = nextindex
            counter += 1

        return counter

    @staticmethod
    def jumpsteps2(registers):
        counter = 0
        index = 0
        while index >= 0 and index < len(registers):
            steps = registers[index]
            nextindex = index + steps
            if steps >= 3:
                registers[index] -= 1
            else:
                registers[index] += 1
            index = nextindex
            counter += 1

        return counter

if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = [int(x) for x in FILE.read().splitlines()]
    FILE.close()
    INDATA2 = copy.copy(INDATA)
    print("Trampolines1: ", Trampolines.jumpsteps1(INDATA))
    print("Trampolines2: ", Trampolines.jumpsteps2(INDATA2))
