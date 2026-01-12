def permute(s, index=0):
    if index == len(s) - 1:
        print("".join(s))
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]  # swap
        permute(s, index + 1)
        s[index], s[i] = s[i], s[index]  # backtrack


permute(list("ABC"))
