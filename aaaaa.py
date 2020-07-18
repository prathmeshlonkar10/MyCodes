f=2
l=6
count=1
for i in range(f, l+1):
    if i==f:
        print('first', i)
        print('C:',count)
    if i==l:
        print('last', i)
        print('C:',count)
    else:
        print(i)
        print('EC:',count)
    count=count+1
