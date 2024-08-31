#Write a function reverse_string(s) that
#takes a string s and returns the reversed version of the string.

s = input("enter a string")
def reverse_string(s):
    return s[::-1]


reversed_string = reverse_string(s)
print(f"Reversed string: {reversed_string}")
