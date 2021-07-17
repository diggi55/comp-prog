# Accepted: Jul/17/2021 15:51UTC+2

def main():
    t = int(input())

    for _ in range(t):
        l, r = map(int, input().split(" "))

        if r < 2*l:
            print("-1 -1")
        else:
            print(l, 2*l)


if __name__ == "__main__":
    main()