def tellmelist():
    print('\nThe entered elements are as follows: ')
    for i in range(len(variable)):
        print (i+1,variable[i])

variable=list()
while True:
    v=input('Enter the variable: ')
    if v=='done':
        break
    variable.append(v)
tellmelist()
