snack = input("Enter your prefferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
  print(f"Great Choice! We'll serve you {snack}")
else:
  print(f"Sorry {snack} is not available. We only serve cookies or samosa.")
