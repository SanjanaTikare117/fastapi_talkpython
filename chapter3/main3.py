import fastapi
import uvicorn
from typing import Optional

# Create an instance of FastAPI
api = fastapi.FastAPI()

# Define a route to perform a calculation
@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z==0:
        return fastapi.Response(content="ERROR:Z cannot be zero",status_code=400)
    value= x+y
    if z is not None:
        value/=z
    return {
        'x':x,
        'y':y,
        'z':z,
        'value':value
    }
uvicorn.run(api,port=1000,host='127.0.0.1')