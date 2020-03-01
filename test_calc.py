import calc

def test_add():
    assert calc.add(7, 3) == 10
    assert calc.add(-7, -1) == -8
    assert calc.add(4.5, 5.3) == 9.8

def test_subtract():
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(7.2, 3.2) == 4
    assert calc.subtract(-4, 3) == -7

def test_product():
    assert calc.product(5, 5) == 25
    assert calc.product(5, 2.5) == 12.5
    assert calc.product(0, 0) == 0

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_product()