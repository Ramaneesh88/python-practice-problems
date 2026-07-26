a=[1,2,3,4,6,5]
max=0
min=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
print("max:",max)
for j in range(len(a)):
    if a[j]<min:
        min=a[j]
print("min:",min)
