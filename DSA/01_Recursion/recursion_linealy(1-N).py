#print(1-n)linearly
def print_linear(i,n):
    if i<1:
        return
    print(i)
    print_linear(i-1,n)

n = int(input("enter a number"))

print_linear(n,n)
# enter a number5
# 5
# 4
# 3
# 2
# 1

def print_linear(i,n):
    if i>n:
        return
    print(i)
    print_linear(i+1,n)

n = int(input("enter a number"))

print_linear(1,n)
# enter a number5
# 1
# 2
# 3
# 4
# 5