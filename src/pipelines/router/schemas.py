from pydantic import BaseModel
from typing import Literal


class RouterDecision(BaseModel):
    route: Literal["sql", "policy", "smalltalk", "analytics"]
    confidence: float