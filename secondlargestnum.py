def second_larg_optimal(arr):
    if len(arr)<2:
        return "not valid"
    largest=float("-inf")
    second=float("-inf")
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    if second==float('-inf'):
        return "no second largest"
    return second
a=list(map(int,input("Enter the numbers:").split()))
print(second_larg_optimal(a))
