import unittest
from dataclasses import is_dataclass

from main import Product


class TestProduct(unittest.TestCase):

    def test_if_it_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def setUp(self):
        self.product = Product(1, 'Caneta Azul', 2.50, 10)

    def test_constructor(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, 'Caneta Azul')
        self.assertEqual(self.product.price, 2.50)
        self.assertEqual(self.product.stock, 10)

    def test_increase_stock(self):
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 20)

    def test_decrease_stock(self):
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 0)

    def test_check_positive_number(self):
        with self.assertRaises(Exception) as assert_error:
            self.product.check_positive_number(-1)
        self.assertEqual(
            assert_error.exception.args[0], "Number must be positive")

    def test_check_negative_stock(self):
        with self.assertRaises(Exception) as assert_error:
            self.product.decrease_stock(11)
        self.assertEqual(
            assert_error.exception.args[0],
            "Stock must be greater than or equal to 0"
        )


if __name__ == "__main__":
    unittest.main()

# COMANDOS NO TERMINAL

# python -m venv venv
# .\venv\Scripts\activate
# pip install coverage

# CRIA .coverage
# python -m coverage run main_test.py
# python -m coverage run -m unittest discover src/test/

# python -m coverage report

# CRIA htmlcov
# python -m coverage html
