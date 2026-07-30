def arr_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return "array is not sorted"
    return "array is sorted"

a=list(map(int,input("enter the values in an array:").split()))
print(arr_sorted(a))