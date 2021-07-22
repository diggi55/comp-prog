
def transpose():
    nested = [[1, 2, 3], [4, 5, 6]]
    print(nested)
    nested_transposed = [col for col in zip(*nested)]
    print(nested_transposed)

    print(*nested)


# Accepted:

# import math as m
# import itertools as it
# import copy as cp

def main():
    t = int(input())

    for x in range(t):
        n = int(input())

        matrix = [list(map(int, input().split(" "))) for _ in range(n)]

        trace = sum(matrix[i][i] for i in range(n))
        duplicate_rows = sum(len(row) != len(set(row)) for row in matrix)
        duplicate_columns = sum(len(col) != len(set(col)) for col in zip(*matrix))

        print(f"Case #{x + 1}: {trace} {duplicate_rows} {duplicate_columns}")


if __name__ == "__main__":
    main()