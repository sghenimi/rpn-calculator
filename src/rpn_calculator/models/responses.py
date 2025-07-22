from typing import List, Union

from pydantic import BaseModel


class StackResponse(BaseModel):
    stack: List[Union[int, float]]