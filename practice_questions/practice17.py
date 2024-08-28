# Write a program that will take three digits from the user and add the square of each digit.

def Square_Of_Each_Digit(x,y,z ):
    square =( x**2 +y**2 + z**2)
    print(square)


x,y,z = map(int,input().split())

Square_Of_Each_Digit(x,y,z )