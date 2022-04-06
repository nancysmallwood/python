# CurrencyConversionFactors 1 - unlimited
from calcobjects.currencyconversionfactor import CurrencyConversionFactor


class CurrencyConversionFactors:
    # The init method or constructor
    def __init__(self, items):
        self.currency_conversion_factors = [CurrencyConversionFactor(items)]
        if items is not None:
            if isinstance(items, list):
                for item in items:
                    self.currency_conversion_factors.append(CurrencyConversionFactor(item))
            elif isinstance(items, dict):
                self.currency_conversion_factors.append(CurrencyConversionFactor(items))

    def __str__(self):
        pretty_str = ''
        for item in self.currency_conversion_factors:
            pretty_str += '\n %s ' % item
        return pretty_str

    def to_json(self):
        json_str = '['
        number_currency_conversion_factors = len(self.currency_conversion_factors)
        counter = 0
        for item in self.currency_conversion_factors:
            counter += 1
            json_str += item.to_json()
            if counter != number_currency_conversion_factors:
                json_str += ','
        json_str += ']'
        return json_str
