from typing import List, Any, Coroutine, Union

import uvicorn
from fastapi import FastAPI

from src.rpn_calculator.models.responses import StackResponse
from src.rpn_calculator.models.rpn_stack import RpnStack
from src.rpn_calculator.models.stack_item import StackItem
from src.rpn_calculator.models.operations_list import OperationsEnum

app = FastAPI(title="RPN Calculator")

# @app.get("/health")
# async def health():
#     return "OK"

calculator: RpnStack = RpnStack()

@app.get("/api/rpn/current_stack", response_model=StackResponse)
async def current_stack():
    """
    Returns the current stack
    :return: list of stack numbers
    """
    return StackResponse(stack=calculator.get_current_stack())

@app.post("/api/rpn/add_item", response_model=StackResponse)
async def add_item(item: StackItem)-> StackResponse:
    """
    Adds an item to the stack
    :param item:
    :return: list of stack numbers
    """

    calculator.push(float(item.value))

    return StackResponse(stack=calculator.get_current_stack())

@app.post("/api/rpn/calculate")
def calculate(operation: OperationsEnum):
    pass

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)