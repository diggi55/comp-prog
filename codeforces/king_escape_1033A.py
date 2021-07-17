# Accepted:  Jul/11/2021 15:39UTC+2

if __name__ == "__main__":
    n = int(input())
    queen_x, queen_y = [int(i) for i in input().split(" ")]
    king_x, king_y = [int(i) for i in input().split(" ")]
    target_x, target_y = [int(i) for i in input().split(" ")]

    if king_x < queen_x < target_x or \
       target_x < queen_x < king_x or \
       king_y < queen_y < target_y or \
       target_y < queen_y < king_y:
        print("NO")
    else:
        print("YES")
