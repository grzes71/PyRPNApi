"""
Unit tests for RPN Calculator.
"""
from decimal import Decimal
from pyrpnapi.calc import calculate

def test_single_value():
    "Test single value"
    assert calculate('123') == Decimal(123)

def test_add():
    "Test adding"
    assert calculate('1 2 +'.split()) == Decimal(3)

def test_sub():
    "Test substraction"
    assert calculate('150 50 -'.split()) == Decimal(150-50)

def test_mul():
    "Test multiplication"
    assert calculate('4 50 * '.split()) == Decimal(4*50)

def test_div():
    "Test division"
    assert calculate('100 25 /'.split()) == Decimal(100/25)
