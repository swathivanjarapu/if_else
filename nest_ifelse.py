age=int(input("enter age"))
day=int(input("enter days"))
sex=input("enter sex")
if age>=18 and age<30:
    if day==10:
        if sex=='f':
            print(day*700)
        else:
            print(day*750)
elif age>30 and age<=40:
    if day==15:
        if sex=='f':
            print(day*800)
        else:
            print(day*850)
else:
    print("not")
            