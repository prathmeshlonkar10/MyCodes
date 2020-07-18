def invalidcheck(h, m):     # Function for time validation CHECK
        if h<0 or h>23:
            print('\n===== ERROR =====\nInvalid hour input. Try again')
            return('goback')
        if m<0 or m>59:
            print('\n===== ERROR =====\nInvalid minute input. Try again')
            return('goback')
        return('okpass')

while True:
    while True:     # Time input
        st=input('\n\n===== NEW =====\nEnter the time in hh:mm format: ')
        if st=='no':
            print('===== DONE =====')
            quit()
        if ':' not in st:
            print('\n===== ERROR =====\nKindly enter the time in hh:mm format.')
            continue
        list_st=st.split(':')
        if len(list_st)!=2:
            print('\n===== ERROR =====\nKindly enter the time as shown. Example:- hh:mm')
            continue

        shrs=list_st[0]
        smin=list_st[1]

        try:
            hrs=int(shrs)
            min=int(smin)
        except:
            print('\n===== ERROR =====\nKindly enter numeral value only.')
            continue

        ivc=invalidcheck(hrs, min)
        if ivc=='goback': continue

        print('\nTime in 24 hours format:-', shrs, ':', smin)

        if hrs==0:
            hrs=hrs+12
            print('Time in 12 hours format:-', hrs,':', smin)
        elif hrs>12:
            hrs=hrs-12
            print('Time in 12 hours format:-', hrs,':', smin)

        break

    # Degree calculation
    md=min*6

    ihd=hrs*30
    lhd=(md*30)/360
    thd=ihd+lhd

    fa=md-thd

    if fa<0:
        fa=fa*(-1)

    if fa>180:
        fa=360-fa

    print('\nAngle between hour & minute hand is:', fa, 'degrees\n===== DONE =====')
