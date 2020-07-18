while True:
    fn=input('Enter first number: ')
    if fn=='done':
        quit()
    ffn=float(fn)
    o=input('Enter the symbol of operation you want to perform: ')
    sn=input('Enter second number: ')
    fsn=float(sn)
    if o=='+':
        print(ffn+fsn)
    elif o=='-':
        print(ffn-fsn)
    elif o=='*':
        print(ffn*fsn)
    elif o=='/':
        print(ffn/fsn)
    elif o=='^':
        print(ffn**fsn)
