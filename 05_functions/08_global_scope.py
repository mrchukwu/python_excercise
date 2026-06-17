chai_type = "Plain"

def update_order():
  def kitchen():
    global chai_type
    chai_type = "Irani Chai"
  kitchen()
  print("After kitchen update ", chai_type)

update_order()
print("Global chai_type:", chai_type)