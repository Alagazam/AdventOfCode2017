# pylint: disable=missing-docstring

import math

class Manhattan:
    @staticmethod
    def coordinate(n):
        k = math.ceil((math.sqrt(n)-1)/2)
        t = 2*k+1
        m = t * t
        t = t - 1
        if n >= m-t:
            return k-(m-n), -k
        else:
            m -= t

        if n >= m-t:
            return -k, -k+(m-n)
        else:
            m -= t

        if n >= m-t:
            return -k+(m-n), k

        return k, k-(m-n-t)


    @staticmethod
    def distance1(data):
        x, y = Manhattan.coordinate(data)
        return abs(x) + abs(y)

    @staticmethod
    def distance2(data):
        return 0


if __name__ == '__main__':
    print("distance1: " + str(Manhattan.distance1(368078)))
    print("distance2: " + str(Manhattan.distance2(368078)))
