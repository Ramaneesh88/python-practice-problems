def reverse_array(arr):
    rev=[]
    for num in range(len(arr)-1,-1,-1):
        rev.append(arr[num])
    return rev
a=list(map(int,input("Enter the numbers:").split()))
print(reverse_array(a))
       