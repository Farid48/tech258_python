# List

# Collections are ways to store multiple pieces of data in one object
# Lists are most common/simplest collection
# Also known as arrays

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print("This is your shopping list: \n" + str(shopping_list))

print(f"The data types of your shopping list is: {type(shopping_list)}")

print("The first item in your list is: ", shopping_list[0])

print("The last item in your list is: ", shopping_list[-1])

print("The second item currently is: ", shopping_list[1])
shopping_list[1] = "rice"
print("The second item is now: ", shopping_list[1])

print("The length of the list is currently: ", len(shopping_list))
shopping_list.append("carrots")
print("THe length of the list is: ", len(shopping_list))

forgotten_items = ["toffee","coffee"]
shopping_list = shopping_list + forgotten_items
print(shopping_list)

shopping_list.remove("bananas")

shopping_list.pop()
print("Current shopping list: ", shopping_list)

shopping_list.append("watermelon")
print("Current shopping list: ", shopping_list)

forgotten_items2 = ["double cream","lettuce"]
shopping_list += forgotten_items2
print("Current shopping list: ", shopping_list)

shopping_list.remove("lettuce")
print("Current shopping list: ", shopping_list)

shopping_list.pop()
print("Current shopping list: ", shopping_list)