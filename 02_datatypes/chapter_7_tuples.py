# Tuples => its immutable => cant be changed

masala_spcies = ("cardamon", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spcies
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

# Tuples working behind the scene of this piece of code
ginger_ratio, cardmon_ratio = 2, 1
print(f"Ratio is G : {ginger_ratio} and Cardmon : {cardmon_ratio}")

# switching the raio
ginger_ratio, cardmon_ratio = cardmon_ratio, ginger_ratio
print(f"Ratio is G : {ginger_ratio} and Cardmon : {cardmon_ratio}")


# Unpacking tuple

# masala_spice = ("Cardmon", "Cloves", "Cinnamon", "Ginger", "Fennel")
# ginger_ratio, cardmon_ratio, cloves_ratio, cinnamon_ratio, fennel_ratio = masala_spice

# print(f"Masala spices: {ginger_ratio}, {cardmon_ratio}, {cloves_ratio}, {cinnamon_ratio}, {fennel_ratio}")

# Membership test usin IN
# When working with membership, always think of the case sensitive of the characters
print(f"Is ginger in masala spices ? {'giinger' in masala_spcies}")
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spcies}")


print("")