# You run an online tea store.
# If the order amount is more than N300, delivery is free;
# otherwise, it costs N30.

# Task
# Input order_amount
# user ternary operator to decide delivery fee

order_amount = int(input("Enter the order amount: "))

delivery_fee = 0 if order_amount > 300 else 30 # tenary operator.

print(f"Delivery Fee is: {delivery_fee}") 

