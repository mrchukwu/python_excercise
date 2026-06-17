class Chai:
  def __init__(sefl, sweetness, milk_level):
    sefl.sweetness = sweetness
    sefl.milk_level = milk_level
  
  def sip(self):
    print("Sipping chai")

  def add_sugar(self, amount):
    print("added the sugar" + amount)

  def serve_chai(self):
    print("serving chai")

my_chai = Chai(sweetness=3, milk_level=2)
my_chai.add_sugar(3)
my_chai.serve_chai()


