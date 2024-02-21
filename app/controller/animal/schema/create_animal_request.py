from pydantic import BaseModel, Field
from typing import Optional

class Create_animal_request(BaseModel):
      name: str = Field(...,description="Animal name",min_length=3,max_length=50)
      species: str = Field(None ,description="Animal species")
      gender: str = Field(None ,description="Animal gender")