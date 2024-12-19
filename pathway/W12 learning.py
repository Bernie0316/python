# Finding the max or min

numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
         # This number is larger than the largest we had seen so far

         # So it is now the largest we've seen
        largest_so_far = number

print(f"The largest is: {largest_so_far}")
# The largest is: 85

# KEEPING TRACK OF THE ITEM THAT IS THE MAX OR MIN
shopping_cart = [
    ["Chips", 2.99],
    ["bread", 2.50],
    ["milk", 3.19],
    ["ice cream", 6.99],
    ["cheese", 5.99],
    ["cnady", 0.99],
]
max_price = -1
for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")

#The maximum price is: 6.99

# With first item

max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")

# The maximum price is: 6.99
# The product with the maximum price is: Ice Cream