class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: Vector and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: Vector and {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type for *: Vector and {}".format(type(other)))

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

a = Vector(2, 3)
b = Vector(3, 4)
result_add = a + b
result_sub = a - b
result_mul = a * 2.5

print("Сумма a и b:", result_add)
print("Разность a и b:", result_sub)
print("Умножение a на 2.5:", result_mul)
