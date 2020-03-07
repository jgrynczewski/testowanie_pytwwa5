import pytest

import area

def test_circle_area():
    assert area.circle_area(1) == area.math.pi
    assert area.circle_area(0) == 0
    assert abs(area.circle_area(2.1) - 13.85) < 1e-2


def test_values():
    with pytest.raises(IndexError):
        area.circle_area(-1)

def test_types():
    with pytest.raises(TypeError):
        area.circle_area("asd")
        area.circle_area(True)

#
# def test_values():
#     with pytest.raises(ValueError):
#