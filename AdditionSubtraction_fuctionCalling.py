def calc(x, y):
    add=x+y
    sub=x-y
    return(add, sub)

a=input('Entr the first number: ')
fa=int(a)
b=input('Enter the second number: ')
fb=int(b)
print('The addition & subtration is: ',calc(fa, fb))
