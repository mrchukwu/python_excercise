favourite_chais = [
  "Masal Chai",
  "Ginger Chai",
  "Masal Chai",
  "Mint Chai",
  "Ginger Chai",
  "Elachi Chai",
  "Mint Chai",
]

unique_chai = {chai for chai in favourite_chais }

print(unique_chai)

recipes = {
  'Masal Chai' : ["Water", "Milk", "Sugar", "Tea Leaves", "Masala Powder"],
  'Ginger Chai' : ["Water", "Milk", "Sugar", "Tea Leaves", "Ginger"],
  'Mint Chai' : ["Water", "Milk", "Sugar", "Tea Leaves", "Mint"],
  'Elachi Chai' : ["Water", "Milk", "Sugar", "Tea Leaves", "Elachi"],
  'Lemon Chai' : ["Water", "Milk", "Sugar", "Tea Leaves", "Lemon"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients }

print(unique_spices)