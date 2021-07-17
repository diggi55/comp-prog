# Accepted:  Jul/11/2021 16:09UTC+2

from copy import deepcopy

if __name__ == "__main__":
    def rec(a, lst=[]):
        lst.append(a)
        if a == b:
            return lst
        elif a > b:
            return []

        first_result = rec(a * 2, deepcopy(lst))
        second_result = rec(10 * a + 1, deepcopy(lst))

        return first_result if first_result else second_result


    a, b = [int(i) for i in input().split(" ")]
    result = rec(a)
    if result:
        print("YES")
        print(len(result))
        print(" ".join(str(i) for i in result))
    else:
        print("NO")

