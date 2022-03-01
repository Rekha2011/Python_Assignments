#Question 3:
#We have a string which contains grocery items. Print these items in a comma-separated sequence after sorting them alphabetically.
grocery_items = ' Grated Cheese, Coffee Powder, Pickles, White Chocolate, Dark Chocolate, Eggs, Breads, Milk, Sugar, Salt, Cat Food, Fries'

list_grocery = [word for word in grocery_items.split(', ')]
list_grocery.sort()
list1_grocery = ','.join(list_grocery)
print(list1_grocery)
