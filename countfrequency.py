def count_frequency(a):
    n=len(a)
    dict={}
    for i in range(n):
        val=a[i]
        if val not in dict:
            dict[val]=1
        else:
            dict[val]=dict[val]+1
    return dict

arr=list(map(int,input("enter the numbers to find frequency:").split()))
print("the frequency of the given numbers is:",count_frequency(arr))
