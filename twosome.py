arr=[1,2,4,5,6]
target=6
n=len(arr)
for i in range(n):
  for j in range(i+1,n):
    if arr[i]+arr[j]==target:
      print(i,j)
