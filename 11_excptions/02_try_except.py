chai_menu = {"Masala": 30, "Ginger": 20, "Cardmom": 30}

try:
  chai_menu["Elachi"]
except KeyError:
  print("The Key that your are trying to access does not exist")