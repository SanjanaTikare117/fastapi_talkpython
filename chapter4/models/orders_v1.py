from datetime import datetime
from typing import List, Optional


order_json = {
    'item_id': '123',
    'created_date': '2002-11-24 12:22',
    'pages_visited': [1, 2, '3'],
    'price': 17.22
}

class Order:
    def __init__(self, item_id: int, created_date: str, price: float, pages_visited: Optional[List[int]] = None):
        if pages_visited is None:
            pages_visited = []

        # Convert item_id to int
        try:
            self.item_id = int(item_id)
        except ValueError:
            raise Exception("Invalid item_id, it must be an integer.")
        
        # Convert created_date to datetime
        try:
            self.created_date = datetime.strptime(created_date, '%Y-%m-%d %H:%M')
        except ValueError:
            raise Exception("Invalid created_date, it must be in 'YYYY-MM-DD HH:MM' format.")
        
        # Convert price to float
        try:
            self.price = float(price)
        except ValueError:
            raise Exception("Invalid price, it must be a float.")
        
        # Convert pages_visited to list of integers
        try:
            self.pages_visited = [int(p) for p in pages_visited]
        except ValueError:
            raise Exception("Invalid pages_visited, it must be an iterable containing only integers.")
    
    def __str__(self):
        return str(self.__dict__)


# Create Order object
o = Order(**order_json)
print(o)
