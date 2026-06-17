# Attribute shadowing is when an object property name is deleted and it falls back to the default name in the class level

class Person:
  name = "John"
  age = 32
  career = "UI/UX Designer"

smith = Person()
print(smith.name)

smith.name = "Smith"
smith.career = "Software Engineer"
print(smith.name)
print(smith.career) # it will print the property value name in the object level
print(Person.name)

del smith.career

print(smith.career) # It will fall back to the default name in the class level 