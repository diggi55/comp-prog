# Accepted: Jul/25/2021 21:11UTC+2

#import math as m
#import itertools as it
#import copy as cp


def main():
    t = int(input())

    for _ in range(t):
        l = list(map(int, input().split(" ")))
        ln = sorted(l, reverse=True)

        if (ln[0] == max(l[0], l[1]) or ln[1] == max(l[0], l[1])) and \
            (ln[0] == max(l[2], l[3]) or ln[1] == max(l[2], l[3])):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
