# pylint: disable=missing-docstring

class Checksum:
    @staticmethod
    def calculate1(data):
        total = 0
        for row in data:
            numlist = [int(x) for x in row.split("\t")]
            total += max(numlist) - min(numlist)
        return total

    @staticmethod
    def divisible(num1, num2):
        big = max(num1, num2)
        small = min(num1, num2)
        rem = big % small
        if rem == 0:
            return True, big // small
        return False, 0

    @staticmethod
    def calculate2(data):
        total = 0
        for row in data:
            numlist = [int(x) for x in row.split("\t")]
            div = 0
            for i in range(0, len(numlist)-1):
                for j in range(i+1, len(numlist)):
                    res, div = Checksum.divisible(numlist[i], numlist[j])
                    if res:
                        break
                if div != 0:
                    break

            total += div

        return total


if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = FILE.read().splitlines()
    FILE.close()
    print("checksum1: " + str(Checksum.calculate1(INDATA)))
    print("checksum2: " + str(Checksum.calculate2(INDATA)))
