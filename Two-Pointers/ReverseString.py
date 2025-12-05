import re


def ReverseStrig(n: str) -> str:
    l = list(re.split(" ", n))
    ln = len(l)
    left, right = 0, ln - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return " ".join([word for word in l])


n = "hello world"
print(ReverseStrig(n))
