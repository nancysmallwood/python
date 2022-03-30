# SourceCurrency	1
# TargetCurrency	1
# ConversionFactor	1	Decimal
from calcobjects.currency import Currency
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key


class CurrencyConversionFactor:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'sourcecurrency') is not None:
            self.source_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'sourcecurrency')))
        else:
            self.source_currency = None
        if get_dic_key(dic, 'targetcurrency') is not None:
            self.target_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'targetcurrency')))
        else:
            self.target_currency = None
        # Fields
        self.conversion_factor = get_dic_item(dic, get_attr_key(dic, 'conversionfactor'))

    def __str__(self):
        print_str = "source_currency = %s, target_currency = %s, conversion_factor = %s" \
                    % (self.source_currency, self.target_currency,self.conversion_factor)
        return print_str
