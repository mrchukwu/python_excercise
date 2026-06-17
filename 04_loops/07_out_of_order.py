flavours = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]

for flavour in flavours:
  if flavour == "out of stock":
    continue
  if flavour == "discontinued":
    print(f"{flavour} found")
    break
  print(f"{flavour} found")

print("Tea break ended")