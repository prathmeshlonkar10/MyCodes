mm_30=[4,6,9,11]
mm_31=[1,3,5,7,8,10,12]

def invalidcheck(dd, mm, yy):  # Function for Invalid input date number CHECK
    if dd<1 or dd>31:   # date limit
        print('\n=== ERROR ===\nInvalid Date input. Try again')
        return('goback')
    if mm<1 or mm>12:   # month limit
        print('\n=== ERROR ===\nInvalid Month input. Try again')
        return('goback')
    if mm==2 and (dd==30 or dd==31):    # february limit
        print('\n=== ERROR ===\n30th & 31st February do not exist. Try again')
        return('goback')
    if (mm in mm_30) and dd==31:    # months with 30 days limit
        print('\n=== ERROR ===\n31st does not exist in this month. Try again')
        return('goback')
    if yy<1 or yy>9999:     # year limit
        print('\n=== ERROR ===\nInvalid Year input. Try again')
        return('goback')
    if (yy%4!=0) and mm==2 and dd==29:  # leap year limit 1 for february
        print('\n=== ERROR ===\n(1) 29th February cannot exist except for leap years. Try again')
        return('goback')
    if (yy%100==0 and yy%400!=0) and mm==2 and dd==29:  # leap year limit 2 for february
        print('\n=== ERROR ===\n(2) 29th February cannot exist except for leap years. Try again')
        return('goback')
    return('okpass')

def formatcheck(d):            # Function for incorrect date "." format CHECK
    if '.' not in d:
        print('\n=== ERROR ===\nKindly Enter the date in dd.mm.yyyy format ONLY, using DOTS')
        return('wrongformat')
    return('allFine')

def leapcheck(yy):             # Function for leap year CHECK
    if yy%4==0:
        return('ly')
    if yy%100==0 and yy%400==0:
        return('ly')
    else: return('nly')

def arrange(q,w,e,r,t,y):      # Function to print the final order of dates
    print('\n\n===== After Conversion =====\nDate1:', q,'/', w,'/', e,'\nDate2:', r,'/', t,'/', y)

def result(ans):               # Function to print the final result
    print('\n\n===== RESULT =====\nNumber of days from Date1 to Date2(inclusive):', ans, '\n')
    quit()

while True: # Input for First date
    d1=input('\nEnter Date1 in dd.mm.yyyy format: ')

    form=formatcheck(d1)    # CHECK on correct "." format
    if form=='wrongformat': continue
    list_d1=d1.split('.')
    if len(list_d1) != 3 :
        print('\n=== ERROR ===\nKindly Enter the date seperating dd, mm, yyyy using TWO DOTS.\nExample: dd.mm.yyyy')
        continue

    dd1=list_d1[0]
    mm1=list_d1[1]
    yy1=list_d1[2]

    try:    # Integer value CHECK (No letters allowed)
        dd1=int(dd1)
        mm1=int(mm1)
        yy1=int(yy1)
    except:
        print('\n=== ERROR ===\nKindly Enter numeral values only')
        continue

    ivc=invalidcheck(dd1, mm1, yy1)   # Invalid Date CHECK
    if ivc=='goback': continue

    break

while True: # Input for Second date
    d2=input('\nEnter Date2 in dd.mm.yyyy format: ')

    form=formatcheck(d2)    # CHECK on correct "." format
    if form=='wrongformat': continue
    list_d2=d2.split('.')
    if len(list_d2) != 3 :
        print('\n=== ERROR ===\nKindly Enter the date seperating dd, mm, yyyy using TWO DOTS.\nExample: dd.mm.yyyy')
        continue

    dd2=list_d2[0]
    mm2=list_d2[1]
    yy2=list_d2[2]

    try:    # Integer value CHECK (No letters allowed)
        dd2=int(dd2)
        mm2=int(mm2)
        yy2=int(yy2)
    except:
        print('\n=== ERROR ===\nKindly Enter numeral values only')
        continue

    ivc=invalidcheck(dd2, mm2, yy2)   # Invalid Date CHECK
    if ivc=='goback': continue

    break
# ===== Input Process completed with validation =====
print('\n\n===== Input Data =====\nDate1:', dd1,'/', mm1,'/', yy1,'\nDate2:',dd2,'/', mm2,'/', yy2)

days=0  # Counter to store final result of 'days'

# Now, Arrangement of dates as per order of occurence for d1 & d2.
# Exchange values if not in order
if yy1 > yy2:
    temp=yy2
    yy2=yy1
    yy1=temp

    temp=mm2
    mm2=mm1
    mm1=temp

    temp=dd2
    dd2=dd1
    dd1=temp
    # Now, yy1 < yy2
    arrange(dd1, mm1, yy1, dd2, mm2, yy2)

if yy1==yy2:  # Exchanging values of date1 & date2 if such condition occurs
    if mm1 > mm2:
        temp=mm2
        mm2=mm1
        mm1=temp

        temp=dd2
        dd2=dd1
        dd1=temp
        # Now, mm1 < mm2
        arrange(dd1, mm1, yy1, dd2, mm2, yy2)

    if mm1==mm2:  # Exchanging values of date1 & date2 if such condition occurs
        if dd1 > dd2:
            temp=dd2
            dd2=dd1
            dd1=temp
            # Now, dd1 < dd2
            arrange(dd1, mm1, yy1, dd2, mm2, yy2)

        if dd1==dd2:
            result(days)
# ===== Arrangement as per order of occurence completed =====

# Result calculation & display
if yy1==yy2:
    year=leapcheck(yy1)
    if mm1 < mm2:
        for mm in range(mm1, mm2+1):
            if mm==mm1:
                if mm==2 and year=='ly':
                    days=days+(29-dd1)
                    continue
                if mm==2 and year=='nly':
                    days=days+(28-dd1)
                    continue
                if mm in mm_30:
                    days=days+(30-dd1)
                    continue
                if mm in mm_31:
                    days=days+(31-dd1)
                    continue
            if mm==mm2:
                days=days+dd2
                continue
            else:
                if mm==2 and year=='ly':
                    days=days+29
                if mm==2 and year=='nly':
                    days=days+28
                if mm in mm_30:
                    days=days+30
                if mm in mm_31:
                    days=days+31
        result(days)
    else:   # mm1==mm2
        days=dd2-dd1
        result(days)
# to be cntd...with else
else:   # yy1 < yy2
    for yy in range(yy1, yy2+1):
        year=leapcheck(yy)
        if yy==yy1:
            for mm in range(mm1, 13):
                if mm==mm1:
                    if mm==2 and year=='ly':
                        days=days+(29-dd1)
                        continue
                    if mm==2 and year=='nly':
                        days=days+(28-dd1)
                        continue
                    if mm in mm_30:
                        days=days+(30-dd1)
                        continue
                    if mm in mm_31:
                        days=days+(31-dd1)
                        continue
                else:
                    if mm==2 and year=='ly':
                        days=days+29
                    if mm==2 and year=='nly':
                        days=days+28
                    if mm in mm_30:
                        days=days+30
                    if mm in mm_31:
                        days=days+31
            continue
        if yy==yy2:
            for mm in range(1, mm2+1):
                if mm==mm2:
                    days=days+dd2
                    continue
                else:
                    if mm==2 and year=='ly':
                        days=days+29
                    if mm==2 and year=='nly':
                        days=days+28
                    if mm in mm_30:
                        days=days+30
                    if mm in mm_31:
                        days=days+31
            continue
        else:
            for mm in range(1, 13):
                if mm==2 and year=='ly':
                    days=days+29
                if mm==2 and year=='nly':
                    days=days+28
                if mm in mm_30:
                    days=days+30
                if mm in mm_31:
                    days=days+31
    result(days)
# ===== DONE =====
