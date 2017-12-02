# pylint: disable=missing-docstring

class Captcha:
    @staticmethod
    def calculate1(captcha):
        c_len = len(captcha)
        total = 0
        for index in range(c_len):
            if captcha[index] == captcha[(index + 1) % c_len]:
                total += int(captcha[index])

        return total

    @staticmethod
    def calculate2(captcha):
        c_len = len(captcha)
        total = 0
        for index in range(c_len):
            if captcha[index] == captcha[(index + c_len // 2) % c_len]:
                total += int(captcha[index])

        return total

if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = FILE.readline().rstrip('\n')
    FILE.close()
    print("Captcha1: " + str(Captcha.calculate1(INDATA)))
    print("Captcha2: " + str(Captcha.calculate2(INDATA)))
