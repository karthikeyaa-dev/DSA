def SortedSquare(n: list) -> list:
    l = len(n)
    res = [0] * l
    left, right = 0, l - 1

    for i in range(l - 1, -1, -1):
        if abs(n[left]) > abs(n[right]):
            v = n[left]
            left += 1
        else:
            v = n[right]
            right -= 1

        res[i] = v**2

    return res


def AnotherMethod(n: list) -> list:
    l = len(n)
    res = [0] * l
    left, right = 0, l - 1
    pos = l - 1

    while left <= right:
        if abs(n[left]) > abs(n[right]):
            res[pos] = n[left] ** 2
            left += 1
        else:
            res[pos] = n[right] ** 2
            right -= 1
        pos -= 1

    return res


n = [-1, 0, 1, 2]
print(SortedSquare(n))
print(AnotherMethod(n))
