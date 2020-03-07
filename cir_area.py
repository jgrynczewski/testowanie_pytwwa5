import math

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Niepoprawny typ wartości wejściowej.")
    if r<0:
        raise ValueError("Koło o zadanym promieniu nie istnieje.")
    try:
        return math.pi*r**2
    except:
        raise Exception("Coś poszło nie tak")

# print(circle_area(1))
# print(circle_area(0))
# print(circle_area(-1))
# print(circle_area(2+5j))
# print(circle_area(True))
# print(circle_area("asd"))

