units=int(input("enter the how many units:"))
if units<=100:
    a=units*1.5
    print("the electricity bill is:",a)
elif units>100 and units<=200:
    b=units*2.5
    print("the electricity bill is:",b)
else:
    c=units*4
    print("the electricity bill is:",c)
