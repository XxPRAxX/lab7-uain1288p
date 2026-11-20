import math

def calc(t, a, b=0):
    # t = tipo de figura
    if t == "circulo":
        r = a * a * 3.14159
        return r
    elif t == "rectangulo":
        r = a * b
        return r
    elif t == "triangulo":
        r = a * b / 2
        return r
    else:
        return -1

print(calc("circulo", 5))
print(calc("rectangulo", 4, 6))
print(calc("triangulo", 3, 8))