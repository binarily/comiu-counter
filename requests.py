from typing import List

from pydantic import BaseModel


class Colour(BaseModel):
    colour: int
    segment: int


class OrderId(BaseModel):
    id: int


class Element(BaseModel):
    sku: int
    quantity: int


class OrderRequest(BaseModel):
    orderId: OrderId
    elements: List[Element]


class OrderColourRequest(BaseModel):
    orderId: OrderId
    status: str
    colour: Colour
