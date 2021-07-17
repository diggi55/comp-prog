# Accepted: Jul/17/2021 16:15UTC+2

import math as m

def main():
    t = int(input())

    for _ in range(t):
        e = int(input())
        w = 100 - e

        g = m.gcd(e, w)
        print(int(e/g + w/g))


if __name__ == "__main__":
    main()