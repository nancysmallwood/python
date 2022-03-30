# CurrencyConversionFactors 1 - unlimited
from calcobjects.currencyconversionfactor import CurrencyConversionFactor


class CurrencyConversionFactors:
    # The init method or constructor
    def __init__(self, items):
        self.currency_conversion_factors = []
        if isinstance(items, list):
            for item in items:
                self.currency_conversion_factors.append(CurrencyConversionFactor(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.currency_conversion_factors:
            pretty_str += '\n %s ' % item
        return pretty_str
