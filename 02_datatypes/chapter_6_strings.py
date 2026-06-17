chaai_type = "Ginger chai"
customer_name = "Kennedy"

print(f"Order for {customer_name} : {chaai_type} please !")

chai_descriptioon = "Aromatic and Bold"
print(f"First Word: {chai_descriptioon[0:8]}")
print(f"First Word: {chai_descriptioon[0:8:2]}") #last digit means skip character
print(f"First Word: {chai_descriptioon[:8]}")
print(f"Last Word: {chai_descriptioon[12:]}") # get the lat word
print(f"Reverse Word: {chai_descriptioon[: : -1]}") # short-hand to reverse the string

# encoding characters
label_text = "Chai Speacial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")

# decode
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

