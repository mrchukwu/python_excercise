# Smart Thermostat System

## You're building a smart thermostst alert system:
## If the device_status is "active"
##  And temprature > 35 -. Warn: "Hight temprature alert!"
##  Else: "Temprature normal"
# If device is off -> "Device is offline"

device_status = "active"
temprature = 38

if device_status == "active":
  if temprature > 35:
    print("High temprature alert!")
  else:
    print("Temprature normal")
else:
  print("Device is offline")