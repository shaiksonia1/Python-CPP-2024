# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num = input("enter a 4 digit number")

if len(num) != 4 or not num.isdigit():
    print("invalid input ,  enter a 4 digit number")
else:
    reversed_num = num[::-1]
if num ==  reversed_num:
    print(f"The reverse is equal to the original number: {reversed_num}")
else:
    print(f"The reverse is not equal to the original number: {reversed_num}")


     