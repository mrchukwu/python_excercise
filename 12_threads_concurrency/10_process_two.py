# import threading
from multiprocessing import Process
import time

def cpu_heavy():
  print(f"Crunching some numbers...")
  total = 0
  for i in  range(10**7):
    total += 1
  print("Done ✅")

if __name__ == "__main__":
  start = time.time()
  # threads = [threading.Thread(target=cpu_heavy) for i in range(2)]
  processes = [Process(target=cpu_heavy) for i in range(2)]
  [p.start() for p in processes]
  [p.join() for p in processes]

  end = time.time()
  print(f"Total time: {end - start:.2f} seconds")