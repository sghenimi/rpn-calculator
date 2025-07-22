import uvicorn
from fastapi import FastAPI

app = FastAPI(title="RPN Calculator")

@app.get("/health")
async def health():
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)