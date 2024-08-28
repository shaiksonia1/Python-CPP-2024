# Write a program to find the euclidean distance between two coordinates.

import math
def Euclidean(x1,y1,x2,y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(f"euclidean distance between two coordinates is ,{d}")
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
Euclidean(x1,y1,x2,y2)
