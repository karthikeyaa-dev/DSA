def DiceProblem(dice1, dice2):
    target = 9
    result = set()
    
    for i in range(len(dice1)):
        for j in range(len(dice2)):
            if dice1[i] + dice2[j] == target:
                result.add((dice1[i], dice2[j]))

    return [list(t) for t in result]


dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

print(DiceProblem(dice1, dice2))
