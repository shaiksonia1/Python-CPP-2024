# variables
#here x,y,z are variables, variables means a container whcih can store the values we can assign multiple varaibles at atime
x,y,z = 10,20,20
print(x,y,z)

a = 10
b = 90
print(a+b)
print(type(a))

# id
#id is a built in function in python it return unique identifier
my_var = 10
new_var = 89
print(id(my_var))
print(id(new_var))

my_var = 89
print(id(my_var))

a = ["ball", "car"]
b = ["ball", "car"]
print(id(a))
print(id(b))

#strings
# strings are squence of characters in python
print(type("sonia"))

s = 'codewithaish'
print(s)
c= f"hello it's codewithaish i love to code"
print(c)

#boolean
# it returns also TRUE AND FALSE

d = True
print(type(d))

e = 8
f = 20
g = e > f
print(g)

print(type(e))
print(type(f))
print(type(g))

#none datatype

x = 10
y  = print(x)
print(y)
print(type(y))


a = 8

print(a**3)

# arthmetic operatos
a = int(input("enter a number"))
b = int(input("enter a number"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b) #floor division

# relational operators

print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

#while using comparions operators in string the value are based on the unicode and it will return the result based on that evaluation

m = 'sonia'
n = 'shaik'
print(ord('s')) #this will give the unicode of characters
print(m<n)


#if else statements

if a < b:
    print("yes")
else:
    print("no")
print("end")


#nested if else

if a>b :
    print("a is greater than b :", a)
elif a<b:
    print("a is less than b:", b)
elif a==b:
    print(" a is equal to b ")
else:
    print("i dont know")

x = range(5,20)
print(x)



