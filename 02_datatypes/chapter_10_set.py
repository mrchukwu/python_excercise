# SET -> unique items, no indexing, unordered

essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # Union
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # Intersection
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential sp[ices: {only_in_essential}]")

# Membership Tests
print(f"Is cloves in optional spices ? {"cloves" in optional_spices}")
