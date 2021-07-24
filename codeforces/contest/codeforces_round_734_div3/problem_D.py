# Accepted:

# import math as m
# import itertools as it
# import copy as cp

def main():
    def e(x):
        return x % 2 == 0
    def o(x):
        return not e(x)

    def solve(n, m, k):
        if e(m):
            if k > m/2:
                return solve(n-1, m, k-m/2)
            else:
                if o(n):
                    return k == n
                else:
                    if k > n:
                        return solve(n, m-2, k-n)
                    else:
                        return e(n-k)
        else:
            if o(n):
                return False
            else:
                return solve(m, n, n*m/2 - k)

    t = int(input())

    for _ in range(t):
        n, m, k = map(int, input().split(" "))
        result = solve(n, m, k)
        print("YES" if result else "NO")

if __name__ == "__main__":
    main()
