
from fastapi import FastAPI
from pydantic import BaseModel
from pyrpnapi.calc import calculate

app = FastAPI()


class Expression(BaseModel):
    expr: str


@app.post("/eval/")
async def evaluate(expression: Expression):
    value = calculate(expression.expr.split())
    return {"value": value}
