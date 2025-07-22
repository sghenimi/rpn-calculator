from typing import List, Any, Coroutine

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="RPN Calculator")

# @app.get("/health")
# async def health():
#     return "OK"

# pile de la calculatrice
rpn_stack: List[int] = []

@app.get("/current_stack")
async def current_stack()-> dict[str, list[int]]:
    """
    Returns the current stack
    :return: list of stack numbers
    """
    return {"stack": rpn_stack}

@app.post("/add_item")
async def add_item(item: int)-> dict[str, list[int]]:
    """
    Adds an item to the stack
    :param item:
    :return: list of stack numbers
    """
    rpn_stack.append(item)
    return {"stack": rpn_stack}

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)