# Write a program that take a user inputr of three angles and will find out
#  whether it can form a triangle or not.


x, y, z= map(int, input("Enter three numbers separated by space: ").split())

if x>0 and y>0 and z>0 and x+y+z == 180:
    print("it is a traingle")
else:
    print("not a triangle")