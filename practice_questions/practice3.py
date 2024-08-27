#Write a program that will convert celsius value to fahrenheit
# Fahrenheit=(Celsius× 
# 5
# 9
# ​
#  )+32
class temperature:
    def __init__(self,c):
        self.c = c

    def fahrenheit(self):
     return (self.c * 9/5) + 32

celsius = temperature(3)
fahrenheit_value = celsius.fahrenheit()

print(f"fahrenheit: {fahrenheit_value}")
