def serve_chai(flavor):
  try:
    print(f"Preparing {flavor} chai...")
    if flavor == "unknown":
      raise ValueError("We dont know that flavor")
  except ValueError as e:
    print("Error: ", e)
  else:
    print(f"{flavor} chai is ready!")
  finally:
    print("Thank you for waiting!")

# serve_chai("Masala")
serve_chai("unknown")