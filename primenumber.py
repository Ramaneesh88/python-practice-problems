def is_prime(n):
    if n>=1:
        for i in range(2,n):
            if n%i==0:
                return "not a prime number"
        return "a primenumber"
    else:
        return "not a prime number"
d=int(input("enter the number to check whether it is prime or not : "))
print(is_prime(d))