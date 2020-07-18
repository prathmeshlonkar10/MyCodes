fib=[1,1]
n=input('\nHow many fibonacci numbers do you want: ')
n=int(n)
i=0
if n==1:
    print('[1]')
elif n==2:
    print(fib)
else:
    while i<n-2 :
        fib.append(fib[i]+fib[i+1])
        i=i+1
    print(fib)
