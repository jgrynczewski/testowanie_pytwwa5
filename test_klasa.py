import pytest
import klasa

@pytest.fixture
def car():
    return klasa.Car("BMV")


def test_car_init(car):
    assert car.model == "BMV"
    assert car.color == "black"


def test_car_change_color(car):
    car.change_color("red")
    assert car.color == "red"


if __name__ == "__main__":
    test_car_init(car)
    test_car_change_color(car)
