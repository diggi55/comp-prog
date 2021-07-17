# Accepted:  Jul/10/2021 09:34UTC+2

if __name__ == "__main__":
    n = int(input())
    employees = [int(input()) for e in range(n)]

    max_depth = 1
    for e in employees:
        depth_of_e = 1
        while e != -1:
            e = employees[e-1]
            depth_of_e += 1
        max_depth = max(max_depth, depth_of_e)

    print(max_depth)
