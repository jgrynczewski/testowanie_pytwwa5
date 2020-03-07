import calc3

def test_add_two_numbers():
    c = calc3.Calc()
    res = c.add(4, 5)
    assert res == 9

def test_add_three_numbers():
    c = calc3.Calc()
    res = c.add(4, 5, 6)
    assert res == 15

def test_many_numbers():
    c=calc3.Calc()
    res=c.add(3, 4, 5, 10, 10, 10, 10, 10)
    assert res == 62