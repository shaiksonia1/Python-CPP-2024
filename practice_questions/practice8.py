# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

num = input("enter a number")

if len(num) != 4 or not num.isdigit():
    print("invalid input")
else:
    nsum = sum(int(digit)**4 for digit in num)

if nsum == int(num):
    print(f"{num} is a Narcissistic number. {nsum}")
else:
    print(f"{num} is not a Narcissistic number.{nsum}")