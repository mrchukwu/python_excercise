# pyrefly: ignore [missing-import]
from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
  username: str

  @field_validator("username")
  def username_length(cls, v):
    if len(v) < 4:
      raise ValueError("username must be at least 4 characters")
    return v


class Singup(BaseModel):
  password: str
  comfirm_password: str

  @model_validator(mode="after")
  def password_match(cls, values):
    if values.password != values.comfirm_password:
      raise ValueError("passwords do not match")
    return values


