def serve_chai():
  yield "Masal Chai"
  yield "Ginger Chai"
  yield "Mint Chai"
  yield "Elachi Chai"
  yield "Lemon Chai"

stall_chai = serve_chai()

# for chai in stall_chai:
#   print(chai)

def get_chai_list():
  return ["cup 1", "cup 2", "cup 3", "cup 4", "cup 5"]

get_chai_list()

def get_chai_gen():
  yield "cup1"
  yield "cup2"
  yield "cup3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))