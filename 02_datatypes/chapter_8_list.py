# List => mutable => can be changed

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove('water')
print(f"Ingredients after removing water: {ingredients}")

# Adding list together
spice_option = ["ginger", "cardamon"]
ingredients.extend(spice_option)
print(f"Ingredients after adding spice option: {ingredients}")

# instering item at a position
ingredients.insert(2, "chocolates")
print(f"Ingredients after inserting chocolate at position 2: {ingredients}")

# remove last added with pop()
last_item_added = ingredients.pop()
print(f"Ingredients after removing last item: {ingredients}")
print(f"Last item was: {last_item_added}")

# reverse list
ingredients.reverse()
print(f"Ingredients after reversing list: {ingredients}")

# sorting the list with sort()
ingredients.sort()
print(f"Ingredients after sorting list: {ingredients}")

# sorted() without changing the original list
unsorted_ingredients = ['ginger', 'sugar', 'chocolates', 'black tea', 'milk']
sorted_ingredients = sorted(unsorted_ingredients)
print(f"Ingredients after sorting list: {sorted_ingredients}")
print(f"Ingredients before sorting list: {unsorted_ingredients}")

# finding max and min
height_level = [1,2,3,4,5,6,7,8,9]
print(f"Max height level: {max(height_level)}")
print(f"Min height level: {min(height_level)}")

# sum of all 
print(f"Sum of all height levels: {sum(height_level)}")
