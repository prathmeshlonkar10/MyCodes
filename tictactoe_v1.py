mat=[[1,2,3],[4,5,6],[7,8,9]]

# Assignment of number selection to the index
for i,j in enumerate(mat):
    for k,l in enumerate(j):
        if l==6:
            mat[i][k]='X'

# printing the matrix
for i in range(3):
    for j in range(3):
        print(mat[i][j], end="")
    print("")
