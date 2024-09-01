'''Linear search is a method for searching for an element in a collection of elements.
 In linear search, each element of the collection is visited one by one in a sequential fashion to find the desired element. 
 linear search is also called as sequentail search'''

def linearsearch(Arr,key):
    index = 0
    while index < len(Arr):
        if Arr[index] ==key:
            return index
        index = index+1
    return -1

Arr = [21,45,77,89,45,7]
found = linearsearch(Arr,89)
print("result :",found)

# linear time complexity in worst case is O(n)