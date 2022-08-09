from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World this is my new API!"}

@app.get("/myname/{name}")
async def myName(name: str):
    return {"message": f"Hello {name} this is my new API!"}

@app.get("/albuquerque")
async def redirect_typer():
    return RedirectResponse("https://images.pexels.com/photos/13125805/pexels-photo-13125805.jpeg")