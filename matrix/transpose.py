def transpose(matrix):

    transpose = list(zip(*matrix))

    for x in transpose:
        print(x)


matrix = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ]

transpose(matrix)