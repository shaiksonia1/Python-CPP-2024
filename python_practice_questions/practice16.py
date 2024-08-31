# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
# Simple Interest= P×R×T/100



def Simple_Interest(P,R,T):
    SI = (P * R * T /100)
    print(f"Simple_Interest is {SI}")


P,R,T = map(float,input().split())

Simple_Interest(P,R,T)