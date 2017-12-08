# pylint: disable=missing-docstring
import copy

class Realloc:
    @staticmethod
    def maxindex(banks):
        maxval = banks[0]
        maxi = 0
        for index, val in enumerate(banks):
            if val > maxval:
                maxval = val
                maxi = index
        return maxi

    @staticmethod
    def redistribute(banks):
        maxi = Realloc.maxindex(banks)
        blocks = banks[maxi]
        banks[maxi] = 0
        for counter in range(blocks):
            banks[(maxi+counter+1) % len(banks)] += 1
        return banks

    @staticmethod
    def find_loop(banks):
        distributions = []
        distributions.append(banks)
        counter = 0
        new_distr = copy.copy(banks)
        while True:
            counter += 1
            new_distr = Realloc.redistribute(copy.copy(new_distr))
            if new_distr in distributions:
                break
            distributions.append(new_distr)
        loop = len(distributions) - distributions.index(new_distr)
        return counter, loop

if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = [int(x) for x in FILE.read().split("\t")]
    print(INDATA)
    FILE.close()
    print("Reallloc: ", Realloc.find_loop(INDATA))
