# Write a Python program to convert an integer to a string in any base using recursion .


def to_string(n, base):
    conver_tString = "0123456789ABCDEF"
    
    if n < base:
        return conver_tString[n]
    else:
      
        return to_string(n // base, base) + conver_tString[n % base]

print(to_string(835, 6))

