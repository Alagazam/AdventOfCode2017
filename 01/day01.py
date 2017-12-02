class captcha:
    def calculate(captcha):
        clen=len(captcha)
        sum=0
        for index in range ( clen ):
            if captcha[index] == captcha[(index+1)%clen] :
                sum += int(captcha[index])

        return sum

    def calculate2(captcha):
        clen=len(captcha)
        sum=0
        for index in range ( clen ):
            if captcha[index] == captcha[(index+clen//2)%clen] :
                sum += int(captcha[index])

        return sum

if __name__ == '__main__':
    file = open("input.txt", "r")
    input = file.readline().rstrip('\n')
    file.close()
    print("Captcha1: " + str(captcha.calculate(input)))
    print("Captcha2: " + str(captcha.calculate2(input)))
