# pylint: disable=missing-docstring
# pylint: disable=invalid-name

import math
class Grid:
    def __init__(self, size):
        self.origo = size
        self.matrix = [[0 for x in range(self.origo*2+1)] for y in range(self.origo*2+1)]

    def get(self, x, y):
        return self.matrix[x+self.origo][y+self.origo]
    def set(self, x, y, value):
        self.matrix[x+self.origo][y+self.origo] = value



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
        xdir, ydir = 1, 0
        x, y = 0, 0
        grid = Grid(int(math.sqrt(data)))
        n = 1
        grid.set(x, y, n)

        while n < data:
            #walk
            x += xdir
            y += ydir
            #shall we turn?
            if grid.get(x-ydir, y+xdir) == 0:
                xdir, ydir = -ydir, xdir
            n += 1
            grid.set(x, y, n)

        return abs(x) + abs(y)

    @staticmethod
    def first_larger(data):
        xdir, ydir = 1, 0
        x, y = 0, 0
        grid = Grid(int(math.sqrt(data)))
        n = 1
        grid.set(x, y, n)

        while n < data:
            #walk
            x += xdir
            y += ydir
            #shall we turn?
            if grid.get(x-ydir, y+xdir) == 0:
                xdir, ydir = -ydir, xdir
            n = grid.get(x-1, y) + grid.get(x+1, y) + grid.get(x, y-1) + grid.get(x, y+1)
            n += grid.get(x-1, y+1) + grid.get(x+1, y+1) + grid.get(x+1, y-1) + grid.get(x-1, y-1)
            grid.set(x, y, n)

        return n


if __name__ == '__main__':
    print("distance1: " + str(Manhattan.distance1(368078)))
    print("distance2: " + str(Manhattan.distance2(368078)))
    print("first_larger: " + str(Manhattan.first_larger(368078)))
