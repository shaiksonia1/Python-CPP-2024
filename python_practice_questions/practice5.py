# Write a program that will give you the sum of 3 digits

num = input("enter a num")

if len(num) != 3 or not num.isdigit():
    print("invalid input , please ente a 3 digit number")

else:
    digit_sum = sum(int(digit) for digit in num)

print(f"Sum of the digits: {digit_sum}")
