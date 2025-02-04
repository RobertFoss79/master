# Problem: Shopping Cart Management

# 1. Create a list called cart with the following items: "milk", "bread", "butter", "cheese", "eggs", "apples".

# 2. Print the entire list of items.

# 3. Calculate and print the total number of items in the cart.

# 4. Check if "bananas" is in the cart and print the result.

# 5. Add "bananas" and "orange juice" to the cart.

# 6. Remove the second item from the cart.

# 7. Sort the list of items in alphabetical order and print the sorted list.

cart = ["milk", "bread", "butter", "cheese", "eggs", "apples"]
print(cart)
print("Number of items:", len(cart))

if "bananas" in cart:
    print("Bananas are in the cart")
else:
    print("There are no bananas in the cart")

cart.append("bananas")
cart.append("orange juice")
del cart [1]

cart.sort()
print(cart)
