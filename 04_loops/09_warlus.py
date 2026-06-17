# value = 13
# remiander = value % 5  

# if remiander:
#   print(f"Not divisible, remiander is {remainder}")

# Using Walrus Operator
value = 13
if remainder := value % 5: # with walrus this syntax is allowed
  print(f"Not divisible, remiander is {remainder}")
else:
  print("There is no remainder")


# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#   print(f"We have {requested_size} in stock")
# else:
#   print("We don't have that size in stock")


flavors = ["masala", "ginger", "lemon", "mint"]
print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
  print(f"Sorry, {flavor} is not available")
print(f"You choose {flavor}. Enjoy your {flavor} tea!")