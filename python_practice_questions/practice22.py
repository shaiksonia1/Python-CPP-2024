
def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11,1): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * N, end=" ") #


multiplicationTable(5)

def stringJumper(str):
    for i in range(0, len(str),2): ## from 0 to length of str and skip 2
        print(str[i], end="")

str = input("enter a name")
stringJumper(str)


def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
        
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code
        print(x, end=" ")
        x -= 1

printInDecreasing(3)