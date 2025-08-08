matrix = [[7,9,1,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
r = len(matrix)
c = len(matrix[0])
rowtrack = [0 for _ in range(r)]
coltrack = [0 for _ in range(c)]
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j] == 0:
            rowtrack[i] = -1
            coltrack[j] = -1
for i in range(0,r):
    for j in range(0,c):
        if rowtrack[i] == -1 or coltrack[j] == -1:
            matrix[i][j] = 0
print(matrix)
