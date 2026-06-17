menu = ["ginger chai", "kadak chai", "masala chai", "green chai", "lemon chai" ]

# Using for loop and enumerate() to print menu items with serial numbers (starting from 1)
for index, item in enumerate(menu, start=1):
    print(f"{index} : {item} chai")