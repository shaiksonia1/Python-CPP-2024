# Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It’s much like the way you might sort playing cards in your hands

def insertionsort(arr):
    n = len(arr)

    for i in range(1,n):
        cvalue =arr[i]
        pos = i
        while pos>0 and arr[pos-1]>cvalue:
            arr[pos] = arr[pos-1]
            pos = pos-1
            arr[pos] = cvalue


arr = [2,8,4,6,10,1,13]

print(arr)
insertionsort(arr)
print("sorted array",arr)