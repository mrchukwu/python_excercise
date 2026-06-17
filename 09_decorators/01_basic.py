from functools import wraps

def my_decorator(func):
  @wraps(func)
  def wrapper():
    print("Before function runs")
    func()
    print("After function runs")
  return wrapper

@my_decorator
def say_hello():
  print("Hello")

say_hello()
print("function name is ",say_hello.__name__)
