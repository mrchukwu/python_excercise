import threading
from os import name
import threading
import time

def bre_chai():
  print(f"{threading.current_thread().name} started brewing...")
  count = 0
  for _ in range(100_000_000):
    count += 1
  print(f"{threading.current_thread().name} brewing completed..")


# create two threads
thread_1 = threading.Thread(target=bre_chai, name="chai_1")
thread_2 = threading.Thread(target=bre_chai, name="chai_2")

start = time.time()
# start thread
thread_1.start()
thread_2.start()


# wait for thread to complete
thread_1.join()
thread_2.join()

end = time.time()

print(f"Time taken by threads: {end - start:.2f}")  
