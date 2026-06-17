base_liquid =  ["water", "milk"]
extra_flavor = ["Cardmon", "Ginger", "Mint"]

print(f"Base Liquid: {base_liquid}")
print(f"Extra Flavor: {extra_flavor}")

# Adding list together
total_ingredients = base_liquid + extra_flavor
print(f"Total Ingredients: {total_ingredients}")

# multiplying items in a list
strong_brew = ["black tea", "watar"] * 3
print(f"Strong Brew: {strong_brew}")

# bytearray
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD") # have to save in a variable (not directly modify)
print(f"Bytes: {raw_spice_data}")
