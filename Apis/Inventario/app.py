from fastapi import FastAPI
from routes.productos import productos
app = FastAPI()

app.include_router(productos)

@app.get('/')

def HelloWorld():
    return "The world is connect!!"