import decimal
from pyrpnapi.calc import calculate

def test_calculate():
    assert calculate('1 2 +'.split())==decimal.Decimal(3)