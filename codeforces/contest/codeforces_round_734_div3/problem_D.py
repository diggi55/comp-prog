# Accepted: Jul/24/2021 20:30UTC+2

# import math as m
# import itertools as it
# import copy as cp

def main():
    def solve(n, m, k):
        # rows are even
        if n % 2 == 0:
            # dominoes are even, so they can build 2x2 bundles
            # this way it's always possible to fill remaining space with vertical dominoes
            if k % 2 == 0:
                # columns are even to be filled up perfectly
                # if not, the leave space for one spare column of vertical dominoes
                if m % 2 == 0 or k <= n * (m - 1) / 2:
                    return True
                else:
                    return False
        # rows are odd
        else:
            # dominoes fill at least one row
            if k >= m / 2:
                # the remaining number of dominoes is even to make up 2x2 bundles
                # and m is even (-> makes sense to test m beforehand,
                # but both attributes can be tested in a simple expression)
                if (k - (m / 2)) % 2 == 0:
                    return True
                else:
                    return False

    t = int(input())

    for _ in range(t):
        n, m, k = map(int, input().split(" "))
        result = solve(n, m, k)
        print("YES" if result else "NO")


if __name__ == "__main__":
    main()
