class checksum:
    def calculate(input):
        sum=0
        for row in input:
            numlist = [int(x) for x in row.split("\t")]
            sum += max(numlist) - min(numlist)
        return sum

if __name__ == '__main__':
    file = open("input.txt", "r")
    input = file.read().splitlines()
    file.close()
    print("checksum1: " + str(checksum.calculate(input)))
    #print("Captcha2: " + str(captcha.calculate2(input)))
