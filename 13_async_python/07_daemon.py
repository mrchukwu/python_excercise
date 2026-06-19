import threading
import time

def monitoring_tea_temp():
  while True:
    print("Monitoring tea temprature...")
    time.sleep(2)

t = threading.Thread(target=monitoring_tea_temp, daemon=True)
t.start()
print("Main program done")