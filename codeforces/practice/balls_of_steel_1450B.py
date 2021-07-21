# Accepted: Jul/20/2021 22:27UTC+2

# import math as m
# import itertools as it
# import copy as cp

def main():
    t = int(input())

    man_d = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    for _ in range(t):
        n, k = map(int, input().split())
        points = [list(map(int, input().split())) for __ in range(n)]

        possible = False

        for p in points:
            max_man_d = max(man_d(p, p_) for p_ in points)
            if max_man_d <= k:
                possible = True
                break

        """
        for p in points:
            in_range = [p_ for p_ in points if man_d(p, p_) <= k]
            if points == in_range:
                possible = True
                break
        """

        print(1 if possible else -1)



    """
    def rec(points, operations):
        # base case: a result was found
        if len(points) == 1:
            return operations

        all_operations = []
        for p in points:
            # remove all point p_ in manhattan distance k of p
            next_points = [p_ for p_ in points if p == p_ or man_d(p, p_) > k]
            # recursion continues as long as points get removed
            if points != next_points:
                all_operations.append(rec(next_points, operations + 1))
            # otherwise, a dead end is reached and the recursion halts to avoid exceeding the stack

        # base case/recursive ascend: no result was found, there are only isolated points remaining
        if not any(all_operations):
            return 0
        # recursive ascend: smallest number of operations is propagated
        return min([op for op in all_operations if op])
    """


if __name__ == "__main__":
    main()
