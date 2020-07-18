# Accounts for all type of wins. Included function definition for result & winner status
mat=[[7,8,9],[4,5,6],[1,2,3]]
# Function definition to display current grid status
def cresult():
    for i in range(3):
        for j in range(3):
            print('\t',mat[i][j], end="")
        print("\n")
# Function definition to display winner message
def congo(x):
    if x==1:
        print('\n========== PLAYER-1 [X] WON ==========')
        quit()
    elif x==2:
        print('\n========== PLAYER-2 [O] WON ==========')
        quit()
# Printing the primary structure here
cresult()
# List of valid input numbers
vnum=[1,2,3,4,5,6,7,8,9]
# Empty list to check repetition of input
rep=[]
# Empty lists to store row & column indices of X & O
rx=[]
cx=[]
ro=[]
co=[]
# Empty dictionaries to store the count of the above obtained indices
posrx={}
poscx={}
posro={}
posco={}
# Counters to account for left & right diagonal wins
lxcount=0
locount=0
rxcount=0
rocount=0
# Loop for valid input, Assignment of input & then-current result status
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
                print('Please enter a SINGLE digit NON-ZERO number only')
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
                            cresult()
                            # Check row or column win for 'X'
                            rx.append(a)
                            cx.append(c)
                            posrx[a]=posrx.get(a,0)+1
                            poscx[c]=poscx.get(c,0)+1
                            #print('posrx:', posrx, '\nposcx:', poscx)
                            if 3 in posrx.values():
                                congo(1)
                            if 3 in poscx.values():
                                congo(1)
                            if a==c :
                                lxcount=lxcount+1
                                if lxcount==3:
                                    congo(1)
                            if (a+c)==2 :
                                rxcount=rxcount+1
                                if rxcount==3:
                                    congo(1)
                break # To come out of while loop only after Assignment is done
        # ========================= SEPERATING X-O ========================= #
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
                print('Please enter SINGLE digit NON-ZERO number only')
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
                            cresult()
                            # Check row or column win for 'O'
                            ro.append(a)
                            co.append(c)
                            posro[a]=posro.get(a,0)+1
                            posco[c]=posco.get(c,0)+1
                            #print('posro:', posro, '\nposco:', posco)
                            if 3 in posro.values():
                                congo(2)
                            if 3 in posco.values():
                                congo(2)
                            if a==c:
                                locount=locount+1
                                if locount==3:
                                    congo(2)
                            if (a+c)==2:
                                rocount=rocount+1
                                if rocount==3:
                                    congo(2)
                break # To come out of while loop only after Assignment is done
    # Same indent as while
# Outside MAIN "for" loop
print('========== GAME DRAW ==========')
