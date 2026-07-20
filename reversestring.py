#method 1 string slicing
n=input("enter the string :")
rev=n[::-1]
print("reverse of the string is :",rev)

#method2 using reversed() function
rev=reversed(n)
print("reverseing of string using reversed() is :",''.join(rev))

#method3 using for loop
rev=""
for str in n:
    rev=str+rev
print("reverse of the string using for loop is :",rev)
