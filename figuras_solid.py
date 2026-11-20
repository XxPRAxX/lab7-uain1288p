import math
from abc import ABC, abstractmethod


class Figura(ABC):
    """Abstraccion comun: toda figura sabe calcular su propia area."""

    @abstractmethod
    def area(self):
        ...


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


class ReporteDeAreas:
    """Unica responsabilidad: mostrar areas. No sabe como se calcula ninguna."""

    def imprimir(self, figuras):
        for figura in figuras:
            print(f"{type(figura).__name__:<12} -> area = {figura.area():.2f}")