r=3
c=3
for i in range(r+1):
    for j in range(c-i):
        print("",end=" ")
    for k in range(c):
        print("*",end=" ")
    print()