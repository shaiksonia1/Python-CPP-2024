# Write a program that will check whether the number is armstrong number or not.
# 153
# Number of digits: 3


def armstrong(num):
   digits = str(num)
   n= len(digits)
   sum_of_num = sum(int(digit)**n for digit in digits)
   return sum_of_num == num

num = int(input("enter a number"))
if armstrong(num):
   print(num, "is an Armstrong number.")

else:
   print(num,"is not an Armstrong number.")