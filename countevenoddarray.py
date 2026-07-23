def even_odd_count(arr):
    count1=0
    count2=0 
    for num in arr:
            if num%2==0:
                count1+=1
            else:
                count2+=1
    return f"even:{count1}, odd:{count2}"
    
a=list(map(int,input("Enter the numbers:").split()))
print(even_odd_count(a))
