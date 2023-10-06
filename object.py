class Car:
    price = 10

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"salom {self.name} uning rangi {self.color}"


obj = Car("Black", "JK")

print(obj)

print(obj.name)
print(obj.color)
print(obj.price)