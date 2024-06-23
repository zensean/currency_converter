class CurrencyExchangeService:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, source, target, amount):
        if source not in self.rates or target not in self.rates[source]:
            return None
        
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Invalid amount provided")

        rate = self.rates[source][target]
        return round(amount * rate, 2)
