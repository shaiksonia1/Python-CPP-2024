def factorial_rec(n):
    if n==0 or n==1:
        return 1
    return factorial_rec(n-1) * n


num = input("enter a number")
n = int(num)

print(factorial_rec(n))