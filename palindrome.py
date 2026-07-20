#method1 using slicing
n=input("enter the string to check whether it is palindrome or not : ")
rev=n[::-1]
if n==rev:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")

#method2 using reversed() function
a=input("enter the string to check whether it is palindrome or not : ")
rev=reversed(a)
rh=''.join(rev)
if a==rh:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome") 

#method3 using for loop
b=input("enter the string to check whether it is palindrome or not : ")
rev=""
for str in b:
    rev=str+rev
if b==rev:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")