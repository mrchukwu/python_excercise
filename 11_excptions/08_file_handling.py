# # Older way of doing things

# file = open("order.txt", "w")
# try:
#   file.write("Masal chai - 2 cups")
# finally:
#   file.close()
#   print("File closed")

# another way of writing

with open("order.txt", "w") as file:
  file.write("Masal chai - 2 cups")
  