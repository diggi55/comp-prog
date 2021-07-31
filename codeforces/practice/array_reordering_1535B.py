# Accepted: Jul/25/2021 21:41UTC+2

import math as m
#import itertools as it
#import copy as cp


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ns = list(map(int, input().split(" ")))

        ns.sort(key=lambda x: x % 2)

        good = 0
        for i in range(n-1):
            if ns[i] % 2 == 0:
                good += n - i - 1
            else:
                good += sum(m.gcd(ns[i], ns[j]) > 1 for j in range(i+1, n))

        print(good)



if __name__ == "__main__":
    main()
