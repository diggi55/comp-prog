# Accepted:

import math as m
# import itertools as it
# import copy as cp
import string


def main():
    t = int(input())

    for _ in range(t):
        s = input()
        mp = dict()

        for c in string.ascii_lowercase:
            mp.update({c : s.count(c)})

        k = 0
        for v in mp.values():
            if v >= 2:
                k += 1

        k += m.floor(sum([v == 1 for v in mp.values()]) / 2)

        print(k)


if __name__ == "__main__":
    main()
