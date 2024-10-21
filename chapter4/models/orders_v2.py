from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Input JSON data
order_json = {
    'item_id': '123',
    'created_date': '2002-11-24 12:22',
    'page_visited': [1, 2, '3'],
    'price': 17.22
}

class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime]  # No need for .datetime
    page_visited: List[int]           # Renamed to match the key in JSON
    price: float

# Create Order object, Pydantic will handle type conversions
o = Order(**order_json)
print(o)


def order_api(order:Order):
    pass