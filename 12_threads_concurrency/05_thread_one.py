import threading
import time

def boli_milk():
  print("Boiling milk...")
  time.sleep(2)
  print("Milk Boile...")

def toast_bun():
  print("Toasting bun...")
  time.sleep(3)
  print("Bun toasted...")

boli_milk()
toast_bun()

start = time.time()

thread_1 = threading.Thread(target=boli_milk)
thread_2 = threading.Thread(target=toast_bun)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end = time.time()
print(f"Time taken {end - start} seconds")