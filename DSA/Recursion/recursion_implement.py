# An iterative function will have a loop with a condition
#here we are iterating using loop
def calculate_itr(n):
    while n>0:
        k =n**2
        print(k)

        n = n-1

calculate_itr(4)

#A recursive function will call the function itself.
# to solve smaller instances of the same problem until it reaches a base case (a condition that stops the recursion).
''''
Types of recursion:

1.Tail Recursion
2.Head Recursion
3.Tree Recursion
4.Indirect Recursion
'''
def calculate_rec(n):
    if n>0:
        k = n**2
        print(k) 
        calculate_rec(n-1) #tail Recursion, first the conditions are executed in this
calculate_rec(4)

def calculate_rec(n):
    if n>0:
        calculate_rec(n-1) #head Recursion, first the function is executed and later the condition statements
        k = n**2
        print(k) 
calculate_rec(4)


def calculate_rec(n):
    if n>0:
        calculate_rec(n-1) #tree recursion
        k = n**2
        print(k) 
        calculate_rec(n-1) #tree recursion
calculate_rec(4)

#output for tree recursion

'''
1
4
1
9
1
4
1
'''


    
