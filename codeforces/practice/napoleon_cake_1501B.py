# Accepted: Jul/22/2021 22:18UTC+2

# import math as m
# import itertools as it
# import copy as cp

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        cream = list(map(int, input().split(" ")))

        cream.reverse()
        mx = 0
        for i in range(len(cream)):
            mx = max(mx, i + cream[i])
            cream[i] = i < mx
        cream.reverse()

        print(" ".join(map(lambda x: str(int(x)), cream)))


if __name__ == "__main__":
    main()
