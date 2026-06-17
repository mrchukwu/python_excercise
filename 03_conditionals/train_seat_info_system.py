# You're building a ticket info system for a railway
# Based on seat type, show it's features.sum

# Task:
# Input "sleeper", "AC", "general", "luxury"
# Match using match-case
# Unknown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper, AC, general, luxury): ").lower()

match seat_type:
  case "sleeper":
    print("Comfortable Seating, Pillow, Blanket")
  case "ac":
    print("AC Seating, Pillow, Blanket, Charging Port")
  case "general":
    print("Basic Seating, No Amenities")
  case "luxury":
    print("Premium Seating, Pillow, Blanket, Charging Port, Refreshments")
  case _:
    print("Invalid seat type")