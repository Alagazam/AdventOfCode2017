class checksum:
    def calculate(input):
        sum=0
        for row in input:
            numlist = [int(x) for x in row.split("\t")]
            sum += max(numlist) - min(numlist)
        return sum

    def calculate2(input):
        sum=0
        for row in input:
            numlist = [int(x) for x in row.split("\t")]
            div = 0
            for i in range(0,len(numlist)-1):
                for j in range(i+1,len(numlist)):
                    big = max(numlist[i],numlist[j])
                    small = min(numlist[i],numlist[j])
                    if (big/small == big//small):
                        div = big//small
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
