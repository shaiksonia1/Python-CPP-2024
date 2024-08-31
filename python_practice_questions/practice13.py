# Write a program that will take user input of cost price and 
# selling price and determines whether its a loss or a profit
# Profit = (Selling Price - Cost Price)
# Loss = (Cost Price - Selling Price)

cp,sp = map(int,input("enter 2 values").split())

if sp > cp:
    Profit = (sp - cp)
    print(f" profit is {Profit}")
elif cp>sp:
    loss = (cp-sp)
    print(f"loss is {loss}")
else:
    print("no profit, no loss")