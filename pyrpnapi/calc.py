import os
import operator, decimal
from collections import deque

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculate(elements):
    pile = deque()
    for element in elements:
        if element in OPERATORS:
            fun = OPERATORS[element]
            val1 = decimal.Decimal(pile.pop())
            val2 = decimal.Decimal(pile.pop())
            pile.append(fun(val2, val1))
        else:
            pile.append(decimal.Decimal(element))
    return pile.pop()
