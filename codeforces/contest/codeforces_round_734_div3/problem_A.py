# Accepted:

# import math as m
# import itertools as it
# import copy as cp

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        print(n // 3 + (n % 3 == 1), n // 3 + (n % 3 == 2))

        """
        rem = n % 3
        bs = (n - rem) // 3

        if rem == 0:
            print(bs, bs)
        elif rem == 1:
            print(bs+1, bs)
        else:
            print(bs, bs+1)
        """

if __name__ == "__main__":
    main()
