# Dictionary 

cha_order = dict(type="Masala Chia", size="Large", sugar=2)
print(f"Chai order: {cha_order}")

# Adding to an empty dictionary
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water"
chai_recipe["additives"] = ["ginger", "cardamon", "sugar"]
print(f"Chai Recipe: {chai_recipe}")

# deleting from dictionary
del chai_recipe["liquid"] # can delete specific items
print(f"Chai Recipe: {chai_recipe}")

print(f"Is sugar in the order? {"sugar" in cha_order}")

chai_order = {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}
# print(f"Order ddetails (keys): {cha_order.keys()}") # only keys
# print(f"Order ddetails (values): {cha_order.values()}") # only values
# print(f"Order ddetails (items): {cha_order.items()}") # items -> to get all data (key, value)

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}") # removes last item

# chai_order.pop("sugar")
# print(f"Order after removing sugar: {chai_order}") # remove specific item

extra_spices = {'cardmon': "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Recipe: {chai_recipe}")

chai_size = chai_order["size"]
chai_size_order = chai_order.get("size", "No note") # safe method of grabbing items
print(f"Chai size is: {chai_size_order}")
