# Write a program that will swap numbers

def swapping(a,b):
    a,b = b,a
    print(f"after swap {a,b}")

a,b = map(int,input("enter 2 numbers").split())

swapping(a,b)