# chai = "Ginger chai"

# def prepare_chai(order):
#   print("Preparing ", order)

# prepare_chai(chai)

chai = [1,2,3]

def edit_chai(cup):
  cup[1] = 42
  print("inside the function", cup)

edit_chai(chai)
print("outside the function", chai)


def make_chai(tea, milk, sugar):
  print(tea, milk, sugar)

make_chai("strong", "full cream", "2 spoons") # positional arguments
make_chai(milk="skimmed", tea=" elaichi", sugar="no spoon") # keyword arguments

#mix of positional and keyword arguments must position
def special_chai(*ingredients, **extras):
  print("Ingredients:", ingredients)
  print("Extras:", extras)

special_chai("ginger", "cardmom", "fennel", topping="cream", extra_hot=True)

# def chai_order(order=[]):
#   order.append("Masala")
#   print(order)

def chai_order(order=None):
  if order is None:
    order = []
  # order.append("Masala")
  print(order)

chai_order()
chai_order()