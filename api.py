from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
    return "Welcome to the Test server Lucatang !"
@app.get("/test")
async def test():
    return "test Lucatang"