class ChaiOrder:
  def __init__(self, type_, size):
    self.type_ = type_
    self.size = size

  def summary(self):
    return f"Order type: {self.type_} and size: {self.size}"

order_1 = ChaiOrder("Masala Chai", "Large")
print(order_1.summary())