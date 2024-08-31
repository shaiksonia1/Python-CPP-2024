# User will input (2numbers).Write a program to swap the numbers


def swap(a,b):
    a,b = b, a
    return a,b

a = int(input("enter a num1"))
b = int(input("enter a num2"))

a,b = swap(b,a)

print(f"after swapping : a is {b} ,b is {a}")
