# Accounts for Row & Column wins 

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

rx=[]
cx=[]
ro=[]
co=[]

posrx={}
poscx={}
posro={}
posco={}



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

                            # Current result status
                            for i in range(3):
                                for j in range(3):
                                    print('\t',mat[i][j], end="")
                                print("\n")

                            # Check row or column win
                            rx.append(a)
                            cx.append(c)
                            posrx[a]=posrx.get(a,0)+1
                            poscx[c]=poscx.get(c,0)+1
                            #print('posrx:', posrx, '\nposcx:', poscx)
                            if 3 in posrx.values():
                                print('\n===== PLAYER-1 [X] WON =====')
                                quit()
                            if 3 in poscx.values():
                                print('\n===== PLAYER-1 [X] WON =====')
                                quit()

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
                            # Current result status
                            for i in range(3):
                                for j in range(3):
                                    print('\t',mat[i][j], end="")
                                print("\n")
                            # Check row or column win
                            ro.append(a)
                            co.append(c)
                            posro[a]=posro.get(a,0)+1
                            posco[c]=posco.get(c,0)+1
                            #print('posro:', posro, '\nposco:', posco)
                            if 3 in posro.values():
                                print('\n===== PLAYER-2 [O] WON =====')
                                quit()
                            if 3 in posco.values():
                                print('\n===== PLAYER-2 [O] WON =====')
                                quit()
                break # To come out of while loop only after Assignment is done


    # Same indent as while
    # Need to decide here, whether any player won or not

print('Rx:', rx,'\nCx:', cx)
print('Ro:', ro,'\nCo:', co)
print('===== GAME DRAW =====')
print('posrx:', posrx, '\nposcx:', poscx)
print('posro:', posro, '\nposco:', posco)
