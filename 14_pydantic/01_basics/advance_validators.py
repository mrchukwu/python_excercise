from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
  first_name: str
  last_name: str

 # multiple field validation
  @field_validator("first_name", "last_name")
  def name_must_be_capitalize(cls, v):
    if not v.istitle():
      raise ValueError("Name must be capitalized")
    return v

class User(BaseModel):
  email: str

  @field_validator("email")
  def normalize_email(cls, v):
    return v.lower().strip()


class Age(BaseModel):
  price: str #$4,444

  @field_validator("price", mode="before")
  def parse_price(cls, v):
    if isinstance(v, str):
      return float(v.replace("$", "").replace(",", ""))
    return v

class DateRange(BaseModel):
  start_date: datetime
  end_date: datetime

  @model_validator(mode="after")
  def validate_dates(self):
    if self.start_date >= self.end_date:
      raise ValueError("start_date must be before end_date")
    return self