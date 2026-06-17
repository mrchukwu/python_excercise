# pure funtion
def pure_function(cups):
  return cups * 10

print(pure_function(10))

total_chai = 10

# Impure functions are not recommended
def impure_function(cups):
  global total_chai
  total_chai += cups
  return total_chai

print(impure_function(10))

# Recursive function
def recursive_function(n):
  if n == 0:
    return "All cups poured"
  print("Pouring cup", n)
  return recursive_function(n - 1)

print(recursive_function(5))


# Lambda Functions
chai_types = ["light", "strong", "masala", "ginger", "masala"]

strong_chai = list(filter(lambda chai: chai == "masala", chai_types))