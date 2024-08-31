# Write a program to find the volume of the cylinder. 
# Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math
def vol_of_cylinder(radius,height):
    volume = math.pi*radius**2*height
    volume_liters = volume / 1000
    return volume_liters

def cost_of_milk(volume_liters, cost_per_liter):
    # Calculate the total cost based on the volume in liters
    total_cost = volume_liters * cost_per_liter
    return total_cost

radius=float(input("enter the value"))
height=float(input("enter the value"))

# Calculate the volume of the cylinder
volume_liters = vol_of_cylinder(radius, height)

# Define the cost per liter
cost_per_liter = 40  # Rs per liter

# Calculate the cost of the milk
total_cost = cost_of_milk(volume_liters, cost_per_liter)
volume = vol_of_cylinder(radius,height)
print(f"The volume of the cylinder is: {volume_liters:.2f} ")
print(f"The cost of filling the cylinder with milk is: Rs {total_cost:.2f}")