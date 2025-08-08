matrix = [[5,20,3],[7,-10,9],[1,-52,6]]

rows = len(matrix)
columns = len(matrix[0])
print(rows, columns)
print(matrix)


for i in range (0,rows):
    for j in range(0,columns):
        print(matrix[i][j],end = " ")
    print()