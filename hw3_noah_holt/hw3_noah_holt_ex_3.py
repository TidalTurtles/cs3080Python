# Homework_3_3
# Noah_Holt
# Due: 7 oct 2022
# Inventory
#
# 1) Save inventory to data structure
# 2) make function to print it out
# 3) make function to add items
# 4) make function to delete

def printInventory(inventory):
    # borrowed from format.py in class as assignment says to do
    print('INVENTORY ITEMS'.center(14 + 10, '-'))
    for k, v in inventory.items():
        print(k.ljust(14, '.') + str(v).rjust(10))

def addItem(inventory, item):
    inventory.setdefault(item, 0)
    inventory[item] = inventory[item] + 1


def deleteItem(inventory, item):
    if inventory.keys(item) == 0:
        inventory[item] = inventory[item] - 1


inventoryItems = {'Hand sanitizer': 10, 'Soap': 6, 'Kleenex': 22, 'Lotion': 16, 'Razors': 12}
# test 1
printInventory(inventoryItems)
# test 2
addItem(inventoryItems, 'Advil')
addItem(inventoryItems, 'Advil')
addItem(inventoryItems, 'Advil')
addItem(inventoryItems, 'Advil')
printInventory(inventoryItems)
# test 3
