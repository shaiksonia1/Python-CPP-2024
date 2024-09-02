def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        pos =i
        for j in range(i+1,n):
            if arr[j]<arr[pos]:
                pos = j
        temp =arr[i]
        arr[i] =arr[pos]
        arr[pos] = temp

arr = [12,67,45,6,797,36,23,55]
print(arr)
selectionsort(arr)
print("sorted array",arr)