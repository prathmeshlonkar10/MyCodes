count=0
i=5
while i>=1:
    i=i-count
    while i>=1:
        print(i,end = '')
        i=i-1
    count=count+1
    print('')
    if count==5:
        break
    i=5
quit()
