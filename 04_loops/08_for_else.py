staff = [("Nenye", 25), ("Onyi", 23), ("Smith", 27)]

for name, age in staff:
  if age >= 26:
    print(f"{name} is eligible to manage the staff")
    break
else: 
  print("No one is eligible to manage the staff")