matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
tran=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        tran[j][i]=matrix[i][j]
print("matrix:",matrix)
print("transposed:",tran)