# Problem: Inventory Management

# 1. Create a list called inventory that contains the following items: "sword", "shield", "potion", "armor", "boots".

# 2. Print the entire inventory list.

# 3. Print the total number of items in the inventory.

# 4. Add a new item "helmet" to the end of the list.

# 5. Remove the item "potion" from the list.

# 6. Print the modified inventory list and the new total number of items.

inventory = ["sword", "shield", "potion", "armor", "boots"]
print(inventory)
print(len(inventory))

inventory.append("helmet")
inventory.remove("potion")
print(inventory)
