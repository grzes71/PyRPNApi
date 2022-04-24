"""
Reverse Polish Notation expression calculation
"""
import operator
import decimal
from collections import deque

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculate(elements):
    """
    Calculate the expression.
    """
    pile = deque()
    for element in elements:
        if element, fun in OPERATORS.items():
            val1 = decimal.Decimal(pile.pop())
            val2 = decimal.Decimal(pile.pop())
            pile.append(fun(val2, val1))
        else:
            pile.append(decimal.Decimal(element))
    return pile.pop()
