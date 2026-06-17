names = ["kennedy", "nenye", "oluchi", "chuks", "onyi", "nnenna", "moni"]
bills = [500, 300, 100, 400, 200, 200, 200]

for name, amount in zip(names, bills):
  print(f"{name} paid {amount} naira")