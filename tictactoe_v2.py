# Manual Two-player Tic-Tac-Toe program

mat=[[7,8,9],[4,5,6],[1,2,3]]
# printing this matrix
for x in range(3):
    for y in range(3):
        print('\t',mat[x][y], end="")
    print("\n")

# loop for input, assignment, result...
for i in range(9):
    if i%2==0:
        p1=input('PLAYER-1 [X] turn: ')
        # Assignment of number selection to the index
        for a,b in enumerate(mat):
            for c,d in enumerate(b):
                if d==int(p1):
                    mat[a][c]='X'
    else:
        p2=input('PLAYER-2 [O] turn: ')
        # Assignment of number selection to the index
        for a,b in enumerate(mat):
            for c,d in enumerate(b):
                if d==int(p2):
                    mat[a][c]='O'
    # printing the current result matrix
    for i in range(3):
        for j in range(3):
            print('\t',mat[i][j], end="")
        print("\n")
