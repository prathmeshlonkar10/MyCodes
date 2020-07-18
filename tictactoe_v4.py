# Accounts for Repetition & both types of Invalid Entries(numeral & non-numeral)

mat=[[7,8,9],[4,5,6],[1,2,3]]
# Printing this matrix
for x in range(3):
    for y in range(3):
        print('\t',mat[x][y], end="")
    print("\n")
# List of valid input numbers
vnum=[1,2,3,4,5,6,7,8,9]
# Empty list to check repetition of input
rep=[]
# Loop for valid input, Assignment of input & result status
for i in range(9):
    while True:
        if i%2==0:
            p1=input('PLAYER-1 [X] turn: ')
            # Check for invalid INPUT(other than number)
            try:
                ip1=int(p1)
            except:
                print('Invalid Entry. Please enter a NUMBER only.')
                continue
            # Check for invalid NUMBER(zero or more than one digits)
            if ip1 not in vnum:
                print('Enter a SINGLE NON-ZERO number only')
                continue
            # Check for repetition of input
            if ip1 in rep:
                print('This Position is taken. Select another Position.')
            else:
                rep.append(ip1)
                # Assignment of 'X' to input number index
                for a,b in enumerate(mat):
                    for c,d in enumerate(b):
                        if d==ip1:
                            mat[a][c]='X'
                break # To come out of while loop only after Assignment is done

        # ===== SEPERATING X-O ===== #
        else:
            p2=input('PLAYER-2 [O] turn: ')
            # Check for invalid INPUT(other than number)
            try:
                ip2=int(p2)
            except:
                print('Invalid Entry. Please enter a NUMBER only.')
                continue
            # Check for invalid NUMBER(zero or more than one digits)
            if ip2 not in vnum:
                print('Enter SINGLE digit NON-ZERO number only')
                continue
            # Check for repetition of input
            if ip2 in rep:
                print('This Position is taken. Select another Position.')
            else:
                rep.append(ip2)
                # Assignment of 'O' to input number index
                for a,b in enumerate(mat):
                    for c,d in enumerate(b):
                        if d==ip2:
                            mat[a][c]='O'
                break # To come out of while loop only after Assignment is done

    # Printing(outside while loop & inside for loop) the current result matrix
    for i in range(3):
        for j in range(3):
            print('\t',mat[i][j], end="")
        print("\n")

    # Need to decide here, whether any player won or not 

print('===== GAME DRAW =====')
