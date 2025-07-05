import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El valor del radio no debe ser menor o igual a 0")
        self.radius = radius
       
    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("El valor del radio no debe ser menor o igual a 0")
        self.radius = new_radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        return Circle(self.radius * n)

    def __str__(self):
        return f"El radio del circulo es: {self.radius:.2f}"


circle_value = float(input("Ingrese el radio del círculo: "))
c = Circle(circle_value)

print(c)
print(f"Área: {c.get_area():.2f}")
print(f"Perímetro: {c.get_perimeter():.2f}")
