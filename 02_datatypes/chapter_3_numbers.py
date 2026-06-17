# Integer

black_tea_grams = 14
ginger_tea_grams = 3

total_tea_grams = black_tea_grams + ginger_tea_grams
print(f"Total tea grams: {total_tea_grams}")

# float
price_per_gram = 0.5
total_price = total_tea_grams * price_per_gram
print(f"Total price: {total_price}")

# division
milk_liters = 7
serving = 4
milk_per_serving = milk_liters / serving
print(f"Milk per serving: {milk_per_serving}")

# Dont need the decimal point attached
total_tea_bags = 10
pots = 3
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}")

# left over tea bags
left_over_tea_bags = total_tea_bags % pots
print(f"Left over tea bags: {left_over_tea_bags}")

# scale factor
tea_gas = 2
scale_factor = 3
scale_tea_up = tea_gas ** scale_factor
print(f"Scale tea up: {scale_tea_up}")  

# Separate large numbers for readablity
large_number = 1_000_000
print(f"Large number: {large_number}")  