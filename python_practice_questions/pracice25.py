# Write a program that can find the factorial of a given number provided by the user.

def factorial(n):
    product =1 
    for i in range(1,n+1):

        product *= i
    return product

n = int(input("enter a number"))
 

total_product = factorial(n)
print(f"the value is {total_product}")
