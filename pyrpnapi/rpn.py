"""
RPN Calculator API
"""

from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from pyrpnapi.calc import calculate


app = FastAPI()


class Expression(BaseModel):
    """
    Expression model class.
    """
    expr: str


@app.post("/eval/")
async def evaluate(expression: Expression):
    """
    Evaluate expression API endpoint.
    """
    value = calculate(expression.expr.split())
    return {"value": value}
