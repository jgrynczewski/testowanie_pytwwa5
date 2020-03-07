import sys
import pytest

import zaaw

@pytest.mark.skipif(sys.version_info.major==3, reason="Version of Python is too low." )
def test_add():
    assert zaaw.add(5, 10) == 15
    assert zaaw.add(-1, -4) == -5


@pytest.mark.parametrize("num1, num2, result",
                         [
                             (7, 3, 10),
                             (-2, -1, -3),
                             (0, 0, 0),
                             (4.2, 4.5, 8.7),
                             (-3, 3, 0)
                         ])
def test_2_add(num1, num2, result):
    assert zaaw.add(num1, num2) == result

@pytest.mark.skip(reason="Domyślnie opuszczony")
def test_opuszczony():
    assert 1==1