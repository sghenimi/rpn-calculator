from typing import List, Union

from pydantic import BaseModel
from http.client import HTTPException

from src.rpn_calculator.models.stack_item import StackItem


class RpnStack:
    def __init__(self):
        # La pile de la calculatrice contient des values de types int ou float
        self.rpn_stack = []

    def get_current_stack(self) -> List[Union[int, float]]:
        return self.rpn_stack


    def push(self, new_item:float):
        self.rpn_stack.append(new_item)

    def pop(self):
        if len(self.rpn_stack) > 0:
            return self.rpn_stack.pop()
        else:
            raise IndexError("Attention La pille esrt vide")

    def clear(self):
        self.rpn_stack = []

    def _is_valid_stack(self)-> bool:
        # check si la pile a au moins 2 elements
        if len(self.rpn_stack) < 2:
            raise HTTPException("Requete non valide, la pile doit avoir au moins deux valeurs")