#Binary Search iterative
'''Binary search is a search algorithm used to find the position of a target value within a sorted array.
 It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty. 
 The search interval is halved by comparing the target element with the middle value of the search space.

 The Binary Search Algorithm can be implemented in the following two ways

Iterative Binary Search Algorithm
Recursive Binary Search Algorithm
'''

def binarysearch_iterative(Arr,key):
    l=0
    r =len(Arr)-1
    while l<=r:
        mid = (l+r)//2
        if key ==Arr[mid]:
            return mid
        elif key<Arr[mid]:
            r = mid-1
        elif key>Arr[mid]:
            l = mid+1
    return -1

Arr = [2,34,56,78,90,99,178,567]
found = binarysearch_iterative(Arr,28)

print("Result",found)

#Binary Search using recusrion

def binary_rec(Arr,key,L,R):
    if L>R:
        return -1
    else:
        m = (L+R)//2
        if key == Arr[m]:
            return m
        elif key <Arr[m]:
            return binary_rec(Arr,key,L,m-1)
        elif key > Arr[m]:
            return binary_rec(Arr,key,m+1,R)


Arr = [2,34,56,78,90,99,178,567]
found = binarysearch_iterative(Arr,56)
print("Result",found)
