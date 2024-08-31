# Write a program that will tell whether the given year is a leap year or not.

def leapyear(n):
    if n%4==0 or( n%100!=0 and n%400==0):
        print("it is a leap year")
    else:
        print("not a leap year")

n = int(input("enter the year"))

leapyear(n)
