# Method Resolution Order

class A:
  label = "A: Base class"

class B(A):
  label = "B: Masala Blend"

class C(A):
  label = "C: Ginger Blend"

class D(B, C):
  pass

cup = D()
print(cup.label)
print(D.__mro__) # This helps to show the flow of inheritance

