import unittest
from primos import es_primo


class TestEsPrimo(unittest.TestCase):
    def test_dos_es_primo(self):
        self.assertTrue(es_primo(2))

    def test_cuatro_no_es_primo(self):
        self.assertFalse(es_primo(4))

    def test_uno_y_cero_no_son_primos(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(0))

    def test_negativos_no_son_primos(self):
        self.assertFalse(es_primo(-7))

    def test_primos_conocidos(self):
        for n in (3, 5, 7, 11, 13, 97):
            self.assertTrue(es_primo(n), f"{n} deberia ser primo")

    def test_compuestos_conocidos(self):
        for n in (6, 9, 15, 21, 100):
            self.assertFalse(es_primo(n), f"{n} no deberia ser primo")


if __name__ == "__main__":
    unittest.main()