# Accepted:  Jul/15/2021 11:29UTC+2

import math as m

if __name__ == "__main__":
    t = int(input())
    lr_pairs = [tuple(map(int, input().split())) for i in range(t)]

    sig = lambda x: x / abs(x)
    a_i = lambda x: x * ((-1) ** x)

    for l, r in lr_pairs:
        result = m.ceil((r - l) / 2) * sig(a_i(r))
        if (l - r) % 2 == 0:
            result += a_i(l)
        print(int(result))
