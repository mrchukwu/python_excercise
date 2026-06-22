from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
  street: str
  city: str
  postal_code: str

class User(BaseModel):
  id: int
  name: str
  address: Address

address = Address(
  street= "123 Aba Road",
  city = "PortHarcourt",
  postal_code = "500231"
)

user = User(
  id = 1,
  name = "John Doe",
  address = address
)

print(user.model_dump())
print(user.address)


user_data = {
  "id": 1,
  "name": "kennedy",
  "address": {
    "street": " 123 main street",
    "city": "PortHarcourt",
    "postal_code": "500231"
  }
}

user = User(**user_data)
print(user.model_dump())