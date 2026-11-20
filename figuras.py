import math


def area_circulo(radio):
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


def main():
    print(f"Area del circulo (radio 5):        {area_circulo(5):.2f}")
    print(f"Area del rectangulo (4 x 6):       {area_rectangulo(4, 6):.2f}")
    print(f"Area del triangulo (base 3, alt 8): {area_triangulo(3, 8):.2f}")


if __name__ == "__main__":
    main()