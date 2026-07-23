#using set to remove duplicates from an array
def remove_duplicates(arr):
    arr=list(set(arr))
    return arr
a=list(map(int,input("Enter the numbers:").split()))
print(remove_duplicates(a))

#using loop to remove duplicates from an array (best for dsa)
def remove_duplicates_loop(arr):
    result=[]
    for num in arr:
        if num not in result:
            result.append(num)
    return result

print(remove_duplicates_loop(a))

#using dictionary to remove duplicates from an array
def remove_duplicates_dict(arr):
    result=list(dict.fromkeys(arr))
    return result
print(remove_duplicates_dict(a))

