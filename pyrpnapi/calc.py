import operator
import decimal


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculate(elements):
    pile = []
    for element in elements:
        if element in operators:
            func = operators[element]
            val1 = decimal.Decimal(pile.pop())
            val2 = decimal.Decimal(pile.pop())
            pile.append(func(val1, val2))
        else:
            pile.append(decimal.Decimal(element))
    return pile[0]
