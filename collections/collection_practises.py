# Level 1

starters = ["salad, garlic bread, wings"]
mains = ["salmon, veg curry, beef stir-fry"]
desserts = ["chocolate cake", "ice cream, apple pie"]

# starter_choice = input(f"Welcome! Please select a starter item: {starters} ")
# main_choice = input(f"Please select one of the following for your main: {mains} ")
# dessert_choice = input(f"Please select one of the following for your dessert: {desserts} ")

#print(f"You have chosen {starter_choice} for your starter. \nYou have chosen {main_choice} as your main. \nYou have chosen {dessert_choice} as your dessert. ")

# Level 2

# customer_order_list = [starter_choice, main_choice, dessert_choice]
# print(customer_order_list)

# Level 3

starter_prices = {
    "salad": 4.99,
    "garlic bread": 7.99,
    "wings": 8.99,
}

main_prices = {
    "salmon": 4.99,
    "veg curry": 7.99,
    "beef stir-fry": 8.99,
}

dessert_prices = {
    "chocolate cake": 4.99,
    "ice cream": 7.99,
    "apple pie": 8.99,
}

starter_choice = input(f"Welcome! Please select a starter item: {starter_prices} ")
main_choice = input(f"Please select one of the following for your main: {main_prices} ")
dessert_choice = input(f"Please select one of the following for your dessert: {dessert_prices} ")

print(f"You have chosen {starter_choice} for your starter. \nYou have chosen {main_choice} as your main. \nYou have chosen {dessert_choice} as your dessert. ")

customer_order_list = [starter_choice, main_choice, dessert_choice]
total = starter_prices[starter_choice] + main_prices[main_choice] + dessert_prices[dessert_choice]
print(f"BIll: \nItems -{customer_order_list} \nTotal - {total} ")