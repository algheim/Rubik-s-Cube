
def reverse(scramble_List):
    #scramble_List = scramble.split(" ")

    solution = []

    for i in range(len(scramble_List) - 1, - 1, -1):
        if len(scramble_List[i]) > 1:
            if scramble_List[i][1] == "'":
                scramble_List[i] = scramble_List[i][0]
                
        else:
            scramble_List[i] += "'"

        solution.append(scramble_List[i])

    return solution
