def move_duplicates_end(n: list) -> list:
    l = len(n)
    write = 0
    for read in range(l):
        if n[read] not in n[:write]:
            n[write] = n[read]
            write += 1

    return n


n = [0, 0, 1, 1, 2, 2, 3]
print(move_duplicates_end(n))
