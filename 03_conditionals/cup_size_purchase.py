cup_size = input("What cup size do you want to buy(small/medium/large): ").lower()

if cup_size == "small":
  price = 10
  print(f"The price of the {cup_size} cup is {price} naira")
elif cup_size == "medium":
  price = 20
  print(f"The price of the {cup_size} cup is {price} naira")
elif cup_size == "large":
  price = 30
  print(f"The price of the {cup_size} cup is {price} naira")
else:
  print(f"{cup_size} is not available. The available sizes are small, medium, large")
