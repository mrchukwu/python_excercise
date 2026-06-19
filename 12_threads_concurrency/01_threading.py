import threading
import time

def take_orders():
  for i in range(1, 4):
    print(f"Taking order for #{1}")
    time.sleep(1)

def brew_chai():
  for i in range(1, 4):
    print(f"Brewing chai #{i}")
    time.sleep(2)

# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# start
order_thread.start()
brew_thread.start()

#  for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed.")