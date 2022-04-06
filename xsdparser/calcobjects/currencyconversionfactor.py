# SourceCurrency	1
# TargetCurrency	1
# ConversionFactor	1	Decimal
from calcobjects.currency import Currency
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_num


class CurrencyConversionFactor:
    # The init method or constructor
    def __init__(self, dic):
        self.source_currency = Currency(dic)
        self.target_currency = Currency(dic)
        self.conversion_factor = None
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'sourcecurrency') is not None:
                self.source_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'sourcecurrency')))
            if get_dic_key(dic, 'targetcurrency') is not None:
                self.target_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'targetcurrency')))
            # Fields
            self.conversion_factor = get_dic_item(dic, get_attr_key(dic, 'conversionfactor'))

    def __str__(self):
        print_str = "source_currency = %s, target_currency = %s, conversion_factor = %s" \
                    % (self.source_currency, self.target_currency,self.conversion_factor)
        return print_str

    def to_json(self):
        return '{"SourceCurrency": %s, ' \
               '"TargetCurrency": %s, ' \
               '"ConversionFactor": %s}' % \
               (self.source_currency.to_json(),
                self.target_currency.to_json(),
                coalesce_num(self.conversion_factor))
