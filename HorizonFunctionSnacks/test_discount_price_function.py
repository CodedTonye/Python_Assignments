from unittest import TestCase
import discount_price_function

class TestDiscountFunctionCorrectness(TestCase):

    def test_save10_code(self):
        result = discount_price_function.get_discounted_price("Shirt", 100.0, "SAVE10")
        self.assertEqual(result, 90.0)

    def test_halfoff_code(self):
        result = discount_price_function.get_discounted_price("Book", 50.0, "HALFOFF")
        self.assertEqual(result, 25.0)

    def test_invalid_code(self):
        result = discount_price_function.get_discounted_price("Lamp", 100.0, "EXPIRED")
        self.assertEqual(result, 100.0)

    def test_zero_price(self):
        result = discount_price_function.get_discounted_price("Freebie", 0.0, "SAVE10")
        self.assertEqual(result, 0.0)

    def test_negative_price(self):
        result = discount_price_function.get_discounted_price("ErrorItem", -10.0, "SAVE10")
        self.assertEqual(result, 0.0)
