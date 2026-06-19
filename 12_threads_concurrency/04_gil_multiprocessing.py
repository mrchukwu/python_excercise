from multiprocessing import Process
import time


def crunc_number():
  print("Staretd the count process...")
  count = 0
  for _ in range(100_000_000):
    count += 1
  print("Ended the count process...")
  
if __name__ == "__main__":
  start = time.time()

  p1 = Process(target=crunc_number)
  p2 = Process(target=crunc_number)

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  end = time.time()
  print(f"Time take to complete {end-start:.2f} seconds")