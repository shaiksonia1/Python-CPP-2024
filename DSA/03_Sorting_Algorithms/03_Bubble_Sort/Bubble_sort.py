def bubblesort(arr):
    n = len(arr)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if arr[i] >arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1] =temp


arr = [54,6,76,34,25,346,7765,45644]
print(arr)
bubblesort(arr)
print("sorted",arr)