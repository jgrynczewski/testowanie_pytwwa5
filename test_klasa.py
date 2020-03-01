import klasa

def test_car_init():
    car = klasa.Car("BMV")
    assert car.model == "BMV"
    assert car.color == "black"

def test_car_change_color():
    car = klasa.Car("BMV")
    car.change_color("red")
    assert car.color == "red"

if __name__ == "__main__":
    test_car_init()
    test_car_change_color()