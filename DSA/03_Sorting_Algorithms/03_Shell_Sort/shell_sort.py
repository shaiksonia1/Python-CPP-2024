def shellsort(a):
    n = len(a)
    gap =n//2
    while gap>0:
        i =gap
        while i<n:
            temp =a[i]
            j =i-gap
            while j>=0 and a[j]>temp:
                a[j+gap]=a[j]
                j = j-gap
            a[j+gap]=temp
            i = i+1
        gap = gap//2

a= [34,54,6,76,85,4635,264,635,323,56,7634,]
print(a)
shellsort(a)
print("sorted arr",a)
        
