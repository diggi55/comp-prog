# Accepted: Jul/24/2021 17:02UTC+2

#import math as m
#import itertools as it
#import copy as cp

def main():
    t = int(input())

    for _ in range(t):
        l, r, d = map(int, input().split(" "))

        if d < l:
            print(d)
        else:
            print(r + (d - (r % d)))

if __name__ == "__main__":
    main()
