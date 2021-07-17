# Accepted:

if __name__ == "__main__":
    t = int(input())
    magnets = [input() for i in range(t)]

    groups = 0
    previous = ""
    for m in magnets:
        if previous != m:
            previous = m
            groups += 1

    print(groups)
