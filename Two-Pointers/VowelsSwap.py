def vowels_swap(n: str):
    ls = [char for char in n]
    lt = len(ls)
    left, right = 0, lt - 1
    Vowels_lib = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    while left < right:
        if ls[left] in Vowels_lib and ls[right] in Vowels_lib:
            swap = ls[left]
            ls[left] = ls[right]
            ls[right] = swap
            left += 1
            right -= 1
        if ls[left] not in Vowels_lib:
            left += 1
        if ls[right] not in Vowels_lib:
            right -= 1
    return "".join([str(char) for char in ls])


n = "leetcode"
print(vowels_swap(n))
