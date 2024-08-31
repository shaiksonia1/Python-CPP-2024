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
def calculate_rec(n):
    if n>0:
        k = n**2
        print(k) 
        calculate_rec(n-1)
calculate_rec(4)