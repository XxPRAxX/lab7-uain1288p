from figuras_solid import Figura


class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2