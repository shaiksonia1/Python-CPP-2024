# Write a program that will tell the number of dogs and 
# chicken are there when the user will provide the value of total heads and legs.

def no_of_heads(dogs,chickens):
    total_head = dogs+chickens
    print(f"total_head is {total_head}" )
def no_of_legs(dogs,chickens):
    total_legs = 4*dogs+ 2*chickens
    print(f"total_legs is {total_legs}")

dogs,chickens = map(int,input().split())

no_of_heads(dogs,chickens)
no_of_legs(dogs,chickens)