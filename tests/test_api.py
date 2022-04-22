"""
Unit tests for RPN Calculator.
"""
import decimal
from pyrpnapi.calc import calculate


def test_add():
    "Test adding"
    assert calculate('1 2 +'.split())==decimal.Decimal(3)

def test_sub():
    "Test substraction"
    assert calculate('150 50 -'.split())==decimal.Decimal(150-50)

def test_mul():
    "Test multiplication"
    assert calculate('4 50 * '.split())==decimal.Decimal(4*50)

def test_div():
    "Test division"
    assert calculate('100 25 /'.split())==decimal.Decimal(100/25)
