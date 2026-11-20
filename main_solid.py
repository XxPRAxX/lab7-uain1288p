from figuras_solid import Circulo, Rectangulo, Triangulo, ReporteDeAreas
from trapecio import Trapecio

figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8),
    Trapecio(6, 4, 3),   # figura nueva, sin tocar figuras_solid.py
]

ReporteDeAreas().imprimir(figuras)