n = int(input("enter a number"))

i = 0
#while loops
while i<=n:
    print(i)
    i = i+1
print("end of program")


#for loops

for i in 'hello':
    print(i)

x=  range(2,8)
print(x)
for i in x:
    print(i)

for i in range(20):
    print(i)


    #break and continue
    #break will exit the loop
    #continue will skip the particular iteration and will continue the loop


n = int(input("enter a value"))
l = [12,34,66,89,4,56]


for i in l :
    print(i,n)
    if i == n:
        print("found")
        break

for i in l:
    print(i,n)
    if i %2==0:
        continue
    print(i)


#lists
#lists are mutable 
l1 =["sonia",10,34]
print(l[0])

l2 =[10,20,30,405,0,5,5]
print(type(l))
print(len(l))

print(l1+l2)

#tuples
#tuples are ordered sequence of data
#tuples are immutable as strings
#tuples are created using elements seperated by commans within parentheses,tuples can have mixed or same type of elements

t = ('sonia',3,34,45.6)

print(type(t))
print(len(t))
print(t[0])
print(t[1])
print(type(t[1]))

#dictionaries
#dict have keys and values
#instead of indices we use keys
#keys are immutable and unique
#dict are defined using curly brackets
#each key value pair is separated by comma
#d = {'usa':100}

d = {'USA':100,'UK':200,'India':300}
print(d)
print(len(d))
print(d['USA']) #to access the values we use keys in dict not index
