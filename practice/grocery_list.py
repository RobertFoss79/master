# Problem: Grocery List Management

# 1. Create a list called grocery_list that contains the following items: "apples", "bananas", "carrots", "detergent", "eggs".

# 2. Print the entire list.

# 3. Print the first and last items in the list.

# 4. Add a new item "flour" to the end of the list.

# 5. Remove the second item from the list.

# 6. Print the modified list.

grocery_list = ['apples', 'bananas', 'carrots', 'detergent', 'eggs']
print(grocery_list)
first_item = grocery_list[0]
print("First Item: ", first_item)
last_item = grocery_list[-1]
print("Last Item: ", last_item)
grocery_list.append("flour")
grocery_list.remove("bananas")
print(grocery_list)
