from typing import Union

from pydantic import BaseModel


class StackItem(BaseModel):
    value: Union[int, float]
