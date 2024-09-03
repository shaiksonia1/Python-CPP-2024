'''

You said:
Python - Namespaces

Write the function definition for the function  'Assign' to assign the different types of variables in its parameters to new variables.

Parameters:

1.An INTEGER in the variable 'i'

2.A FLOAT in the variable 'f'

3.A STRING in the variable 's'

4.A BOOLEAN in the variable 'b'

 

New Variables to be assigned with :

1.An INTEGER in the variable 'w'

2.A FLOAT in the variable 'x'

3.A STRING in the variable 'y'

4.A BOOLEAN in the variable 'z'

 

Assign the parameter variables Respectively.

and

Print these in the following order:

1.w

2.x

3.y

4.z

5.Display all the objects defined in the current namespace by using the 'dir' function

 

Input Format for Custom Testing:

# In the first line, value for 'i'

# In the second line, value for 'f'

# In the third line, value for 's'

# In the fourth line, value for 'b'

 

Sample Test Case 1:

 

Sample Input

STDIN      Function parameter
-----      ------------------
10      →  i
3.14    →  f
One     →  s
True    →  b
 

Sample Output

10
3.14
One
True
['b', 'f', 'i', 's', 'w', 'x', 'y', 'z']
'''

def namespace(i,f,s,b):
    w= i
    x =f
    y=s
    z=b

    print(w)
    print(x)
    print(y)
    print(z)

    print(dir())


namespace(10,43,45,54)
