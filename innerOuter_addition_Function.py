def outer(x, y):
    def inner(p, q):
        add=p+q
        return(add)
    rval=inner(x, y)
    print('The result is:',rval+5)

a=input('Enter first number: ')
fa=int(a)
b=input('Enter second number: ')
fb=int(b)
outer(fa, fb)
