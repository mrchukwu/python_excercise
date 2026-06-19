from multiprocessing import Process, Value

def increament(counter):
  for _ in range(100_000):
    with counter.get_lock():
      counter.value += 1

if __name__ == "__main__":
  counter = Value("i", 0)
  processes = [Process(target=increament, args=(counter, )) for _ in range(4)]
  [p.start() for p in processes]
  [p.join() for p in processes]
  print(f"Final counter: {counter.value}")


