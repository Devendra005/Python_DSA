matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(matrix)
result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(0,n):
    for j in range(0,n):
        result[j][(n-1)-i] = matrix[i][j]
print(matrix)
    
for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(0,n):
    matrix[i].reverse()
print(matrix)