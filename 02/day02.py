class checksum:
    def calculate(input):
        sum=0
        for row in input:
            numlist = [int(x) for x in row.split("\t")]
            sum += max(numlist) - min(numlist)
        return sum

    def divisible(a, b):
        big = max(a,b)
        small = min(a,b)
        div = big/small
        divint = big//small
        if (div == divint):
            return True, div
        return False, 0

    def calculate2(input):
        sum=0
        for row in input:
            numlist = [int(x) for x in row.split("\t")]
            div = 0
            for i in range(0,len(numlist)-1):
                for j in range(i+1,len(numlist)):
                    res, div = checksum.divisible(numlist[i], numlist[j])
                    if (res):
                        break
                if (div != 0):
                    break

            sum += div

        return sum


if __name__ == '__main__':
    file = open("input.txt", "r")
    input = file.read().splitlines()
    file.close()
    print("checksum1: " + str(checksum.calculate(input)))
    print("checksum2: " + str(checksum.calculate2(input)))
