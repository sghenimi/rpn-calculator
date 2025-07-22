from abc import ABC, abstractmethod
from http.client import HTTPException

from src.rpn_calculator.models.rpn_stack import RpnStack

"""
interface commune pour les opérations du calculatrice
"""
class Operation(ABC):

    @abstractmethod
    def execute(self, rpn_stack: RpnStack) -> float:
        pass

class Addition(Operation):
    def execute(self, rpn_stack: RpnStack) -> float:
        rpn_stack._is_valid_stack()
        a = rpn_stack.pop()
        b = rpn_stack.pop()
        res = a + b
        rpn_stack.push(res)
        return res


class Substraction(Operation):
    def execute(self, rpn_stack: RpnStack) -> float:
        rpn_stack._is_valid_stack()
        a = rpn_stack.pop()
        b = rpn_stack.pop()
        res = a - b
        rpn_stack.push(res)
        return res

class Multiplication(Operation):
    def execute(self, rpn_stack: RpnStack) -> float:
        rpn_stack._is_valid_stack()
        a = rpn_stack.pop()
        b = rpn_stack.pop()
        res = a * b
        rpn_stack.push(res)
        return res

class Division(Operation):
    def execute(self, rpn_stack: RpnStack) -> float:
        rpn_stack._is_valid_stack()
        a = rpn_stack.pop()
        b = rpn_stack.pop()
        if b == 0:
            raise HTTPException("Division by zero")
        res = a / b
        rpn_stack.push(res)
        return res


