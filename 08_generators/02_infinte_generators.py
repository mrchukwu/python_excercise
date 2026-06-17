def infinte_chai():
  count = 1
  while True:
    yield f"Refil #{count}"
    count += 1
  
refill = infinte_chai()

for _ in range(5):
  print(next(refill))
  