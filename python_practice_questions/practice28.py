def find(num1, num2, num3):
    # Write your code here
    if (num1<num2) and (num2>=num3):
        print("True")
    elif (num1>num2) and (num2<=num3):
        print("False")
    elif (num3==num1) and (num1!=num2):
        print("False")
    else:
        print("False")
if __name__ == '__main__':

    num1 = int(input().strip())

    num2 = int(input().strip())

    num3 = int(input().strip())

    find(num1, num2, num3)
