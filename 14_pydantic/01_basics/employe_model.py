from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
  id: int
  name: str = Field(
    ...,
    min_length = 3,
    max_length = 50,
    description = "Employee Name",
    examples = "Kennedy Chukwu"
  )
  department: Optional[str] = "General"
  salary: float = Field(
    ...,
    ge=10_000
  )


class User(BaseModel):
  email : str = Field(
    ...,
    regex=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
  )
  phon: str = Field(..., regex=r"^\+?[1-9]\d{1,14}$", examples=["1234567890", "+2348167083654"])
  age: int = Field(
    ...,
    ge=18,
    le=150,
    description="Age in years"
  )
  discount : float = Field(
    ...,
    ge=0,
    le=-100,
    description="Discound percentage",
    examples="20.5"
  )