class Car:
    def __init__(self, model, color="black"):
        self.model = model
        self.color = color

        if model == "Volov":
            self.color = "grey"

    def change_color(self, new_color):
        self.color = new_color