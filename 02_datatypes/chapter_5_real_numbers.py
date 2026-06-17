import sys

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")

# Checking for equality with floating point numbers
is_ideal = ideal_temp == current_temp
print(f"Is temp ideal? {is_ideal}")
print(f"Current temp is ideal: {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")

# float info
print(sys.float_info)
