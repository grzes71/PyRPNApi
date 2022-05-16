"""
RPN Calculator API
"""
from fastapi import FastAPI
from pydantic import BaseModel
from pyrpnapi.calc import calculate


app = FastAPI()


class Expression(BaseModel):
    expr: str


@app.post("/eval/")
async def evaluate(expression: Expression):
    """
    Evaluate the expression and return evalated value.
    """
    value = calculate(expression.expr.split())
    return {"value": value}
