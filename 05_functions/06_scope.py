def serve_chai():
  chai_type = "Masala" # local scope
  print(f"Inside function {chai_type}")

serve_chai()

def main_scope():
  print("From the main scope")
  def inner_scope():
    print("from the inner scope")

  inner_scope()

main_scope()
