# Accepted:

import math as m
#import itertools as it
#import copy as cp

def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split(" "))
        xs = list(map(int, input().split(" ")))

        first_d = xs[0]
        last_d = n - xs[-1] + 1
        res = max(first_d, last_d)

        if k >= 2:
            res = max(res, max([m.floor((xs[i+1] - xs[i]) / 2 + 1) for i in range(k-1)]))

        print(int(res))


if __name__ == "__main__":
    main()
