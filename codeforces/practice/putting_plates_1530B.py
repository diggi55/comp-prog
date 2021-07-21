# Accepted: Jul/21/2021 15:13UTC+2

# import math as m
# import itertools as it
# import copy as cp
import itertools as it


def main():
    t = int(input())

    for _ in range(t):
        h, w = map(int, input().split(" "))

        table = [["0" for w_ in range(w)] for h_ in range(h)]

        for h_ in range(h):
            for w_ in range(w):
                # is on edge:
                if h_ in (0, h-1) or w_ in (0, w-1):
                    # skip if plate is near
                    plate_is_near = False
                    for n in it.product({-1, 0, 1}, {-1, 0, 1}):
                        h__, w__ = h_+n[0], w_+n[1]
                        if h__ in range(h) and w__ in range(w):
                            if table[h__][w__] == "1":
                                plate_is_near = True
                                break
                    if not plate_is_near:
                        table[h_][w_] = "1"

        for row in table:
            print("".join(row))
        print()






if __name__ == "__main__":
    main()
