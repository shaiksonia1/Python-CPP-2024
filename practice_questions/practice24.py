# Write a program to find the sum of first n numbers,
#  where n will be provided by the user. Eg if the user provides n=10 the output should be 55.


def sum_of_number(n):

    total_value = n*(n+1)/2
    return int(total_value)

n = int(input("enter the number"))

value = sum_of_number(n)
print(f"the value is {value}")