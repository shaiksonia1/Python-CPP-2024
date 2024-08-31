# Write  a program that will tell whether the given number is divisible by 3 & 6.


def divisible(n):
    if  n%6==0:
        print(f"it is divisible {n}")
    else:
        print(f"it is not divisble by {n}")

n = int(input("enter a number"))

divisible(n)
