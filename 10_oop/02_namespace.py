class Chai:
  name = "Choco Milo"
  tea_origin = "Nigeria"

my_tea = Chai()
print(my_tea.name)
print(my_tea.tea_origin)

my_tea.brand = "Nigerian beverages"
print(my_tea.brand)

# print(Chai.brand) # doesnt have brand in the class level. Brand is in the object level..

Chai.brand = "Nigerian beverages" # can aslo add to the class level
print(Chai.brand)