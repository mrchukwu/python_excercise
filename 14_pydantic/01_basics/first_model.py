# print("Start of pydantic journey")

# pyright: ignore[missing-import]
from pydantic import BaseModel

class User(BaseModel):
  model_config = {"strict": True} # This line of code puts pydantic on strct mood and avoids coercesion(conversion). It is optional

  id: int
  name: str
  is_active: bool

input_data = {"id": 101, "name": "Chaicode", "is_active": True }

user = User(**input_data)

print(user)