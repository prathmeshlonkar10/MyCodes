mm_30=[4,6,9,11]
mm_31=[1,3,5,7,8,10,12]

endstat=None

def invalidcheck(dd, mm, yy):  # Function for Invalid input date number CHECK
    if dd<1 or dd>31:
        print('\n=== ERROR ===\nInvalid Date input. Try again')
        return('goback')
    if mm<1 or mm>12:
        print('\n=== ERROR ===\nInvalid Month input. Try again')
        return('goback')
    if mm==2 and (dd==30 or dd==31):
        print('\n=== ERROR ===\n30th & 31st February do not exist. Try again')
        return('goback')
    if (mm in mm_30) and dd==31:
        print('\n=== ERROR ===\n31st does not exist in this month. Try again')
        return('goback')
    if yy<1 or yy>9999:
        print('\n=== ERROR ===\nInvalid Year input. Try again')
        return('goback')
    if (yy%4!=0) and mm==2 and dd==29:
        print('\n=== ERROR ===\n(1) 29th February cannot exist except for leap years. Try again')
        return('goback')
    if (yy%100==0 and yy%400!=0) and mm==2 and dd==29:
        print('\n=== ERROR ===\n(2) 29th February cannot exist except for leap years. Try again')
        return('goback')
    return('okpass')

def leapcheck(yy):             # Function for leap year CHECK
    if yy%4==0:
        return('ly')
    if yy%100==0 and yy%400==0:
        return('ly')
    else: return('nly')

def result(dd, mm, yy):           # Function to print the result
    print('\n\n===== RESULT =====\nRequired date:', dd,'/', mm,'/', yy, '\n')
    quit()

while True:     # Loop to keep it going over & over

    while True:     # First date input
        d1=input('\nEnter the starting date in dd.mm.yyyy format: ')
        if d1=='no':
            quit()
        if '.' not in d1:
            print('\n=== ERROR ===\nKindly Enter the date in dd.mm.yyyy format ONLY, using DOTS')
            continue
        list_d1=d1.split('.')
        if len(list_d1)!=3:
            print('\n=== ERROR ===\nKindly Enter the date seperating dd, mm, yyyy using TWO DOTS.\nExample: dd.mm.yyyy')
            continue
        dd1=list_d1[0]
        mm1=list_d1[1]
        yy1=list_d1[2]

        try:
            dd1=int(dd1)
            mm1=int(mm1)
            yy1=int(yy1)
        except:
            print('\n=== ERROR ===\nKindly Enter numeral values only')
            continue
        ivc=invalidcheck(dd1, mm1, yy1)
        if ivc=='goback':
            continue
        break

    while True:     # Number of Days input
        days=input('\nEnter the number of days required after this date: ')
        try:
            days=int(days)
        except:
            print('\n=== ERROR ===\nKindly enter numeral value only')
            continue
        break
    # ========== Input Process Completed ==========

    print('\n\n===== Input Data =====\nStarting from Date:', dd1,'/', mm1,'/', yy1, '\nDays after this Date:', days)

    # to be cntd...
    for yy in range (yy1, 9999+1):
        year=leapcheck(yy)
        if yy==yy1:
            for mm in range(mm1, 12+1):
                if mm==mm1:
                    dd=dd1
                    if mm==2 and year=='ly':
                        remdays=29-dd
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm==2 and year=='nly':
                        remdays=28-dd
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm in mm_30:
                        remdays=30-dd
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm in mm_31:
                        remdays=31-dd
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                else:
                    dd=0
                    if mm==2 and year=='ly':
                        remdays=29
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm==2 and year=='nly':
                        remdays=28
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm in mm_30:
                        remdays=30
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
                    if mm in mm_31:
                        remdays=31
                        if days > remdays:          # Pass the month
                            dd=dd+remdays
                            days=days-remdays
                        else:   # days <= remdays   # In same month
                            dd=dd+days
                            result(dd, mm, yy)
                        continue
            continue
        else:
            for mm in range(1, 12+1):
                dd=0
                if mm==2 and year=='ly':
                    remdays=29
                    if days > remdays:          # Pass the month
                        dd=dd+remdays
                        days=days-remdays
                    else:   # days <= remdays   # In same month
                        dd=dd+days
                        result(dd, mm, yy)
                    continue
                if mm==2 and year=='nly':
                    remdays=28
                    if days > remdays:          # Pass the month
                        dd=dd+remdays
                        days=days-remdays
                    else:   # days <= remdays   # In same month
                        dd=dd+days
                        result(dd, mm, yy)
                    continue
                if mm in mm_30:
                    remdays=30
                    if days > remdays:          # Pass the month
                        dd=dd+remdays
                        days=days-remdays
                    else:   # days <= remdays   # In same month
                        dd=dd+days
                        result(dd, mm, yy)
                    continue
                if mm in mm_31:
                    remdays=31
                    if days > remdays:          # Pass the month
                        dd=dd+remdays
                        days=days-remdays
                    else:   # days <= remdays   # In same month
                        dd=dd+days
                        result(dd, mm, yy)
                    continue
