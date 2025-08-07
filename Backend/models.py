from sqlmodel import SQLModel, Field
from typing import List

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    size: str
    ingredients: List[str] = Field(default_factory=list)

