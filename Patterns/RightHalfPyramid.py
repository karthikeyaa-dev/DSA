def righthalfpyramidpattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()  # This line adds a newline after each row

n = 5
righthalfpyramidpattern(n)
