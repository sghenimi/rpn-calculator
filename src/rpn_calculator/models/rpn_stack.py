from typing import List

from pydantic import BaseModel

from src.rpn_calculator.models.stack_item import StackItem


class RpnStack:
    def __init__(self):
        self.items = items