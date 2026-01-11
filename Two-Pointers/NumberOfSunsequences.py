def NumberOfSubSequences(n: list, target: int) -> int:
    l = len(n)
    n = sorted(n)
    count = 0
    for i in range(l):
        j = i + 1
        while j <= l - 1:
            comp_array = n[i:j]
            if len(comp_array) == 2 and n[i] + n[i] <= target:
                count += 1
            s = max(comp_array) + min(comp_array)
            if s <= target:
                count += 1
                j += 1
            else:
                break
    return count


n = [2, 3, 3, 4, 6, 7]
target = 9
print(NumberOfSubSequences(n, target))
