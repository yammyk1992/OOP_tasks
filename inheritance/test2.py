class Table:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class RoundTable(Table):
    def __init__(self, model, color, radius, height):
        super().__init__(model, color)
        self.radius = radius
        self.height = height
