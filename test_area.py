import pytest

import cir_area

def test_circle_area():
    assert cir_area.circle_area(1) == cir_area.math.pi
    assert cir_area.circle_area(0) == 0
    assert abs(cir_area.circle_area(2.1) - 13.85) < 1e-2


def test_values():
    with pytest.raises(ValueError):
        cir_area.circle_area(-1)

def test_types():
    with pytest.raises(TypeError):
        cir_area.circle_area("asd")
        cir_area.circle_area(True)

#
# def test_values():
#     with pytest.raises(ValueError):
#