inventory = { "Apples": 10,    "Bananas": 5,    "Oranges": 8 }

print(inventory)

#Add new item
inventory["Milk"]=30
print(inventory)

#update existing item(replace old with new)
inventory["Apples"]=20
print(inventory)

#update with adding new value to existing like SUM
inventory["Bananas"]=inventory["Bananas"]+5  # or inventory["Bananas"]+=5
print(inventory)

#delete existing item
del inventory["Apples"]
print(inventory)

for item,qty in inventory.items():
    print(f"{item}: {qty}")
