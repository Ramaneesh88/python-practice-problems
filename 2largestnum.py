def two_largest_num(arr):
    arr=list(set(arr))
    arr.sort()
    if len(arr)>1:
        return arr[-2]
    return -1
a=[1,2,3,4,5]
print(two_largest_num(a))