import unittest
from services.currency_exchange_service import CurrencyExchangeService

class TestCurrencyExchangeService(unittest.TestCase):
    def setUp(self):
        self.rates = {
            "TWD": {
                "TWD": 1,
                "JPY": 3.669,
                "USD": 0.03281
            },
            "JPY": {
                "TWD": 0.26956,
                "JPY": 1,
                "USD": 0.00885
            },
            "USD": {
                "TWD": 30.444,
                "JPY": 111.801,
                "USD": 1
            }
        }
        self.service = CurrencyExchangeService(self.rates)

    def test_convert_success(self):
        result = self.service.convert("USD", "JPY", 1525)
        self.assertAlmostEqual(result, 170496.53, places=1)

    def test_convert_invalid_currency(self):
        result = self.service.convert("EUR", "JPY", 1525)
        self.assertIsNone(result)

    def test_convert_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.service.convert("USD", "JPY", "invalid")

if __name__ == '__main__':
    unittest.main()
