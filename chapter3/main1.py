import fastapi
import uvicorn

api=fastapi.FastAPI()
@api.get('/api/calculate')
def calculate():
    return 2+2

uvicorn.run(api,port=1000,host='127.0.0.1')