# StatisticalValue	0 - 1	Decimal
# Currency	1
# ConversionFactor	1	Decimal
from calcobjects.currency import Currency
from util.dictionary_util import get_attr_key, get_dic_item, coalesce_num, coalesce_str


class StatisticalValue:
    # The init method or constructor
    def __init__(self, dic):
        self.currency = Currency(dic)
        self.statistical_value = None
        if dic is not None:
            self.currency.iso_currency_name = get_dic_item(dic, get_attr_key(dic, 'isocurrencyname'))
            self.currency.iso_currency_code_alpha = get_dic_item(dic, get_attr_key(dic, 'isocurrencycodealpha'))
            self.currency.iso_currency_code_num = get_dic_item(dic, get_attr_key(dic, 'isocurrencycodenum'))
            self.statistical_value = get_dic_item(dic, get_attr_key(dic, 'text'))

    def __str__(self):
        print_str = "iso_currency_name = %s, " \
                    "iso_currency_code_alpha = %s, " \
                    "iso_currency_code_num = %s, " \
                    "statistical_value = %s" \
                    % (self.currency.iso_currency_name,
                       self.currency.iso_currency_code_alpha,
                       self.currency.iso_currency_code_num,
                       self.statistical_value)
        return print_str

    def to_json(self):
        return '{"value": %s, ' \
               '"isoCurrencyName": %s, ' \
               '"isoCurrencyCodeAlpha": %s, ' \
               '"isoCurrencyCodeNum": %s}' % \
               (coalesce_num(self.statistical_value),
                coalesce_str(self.currency.iso_currency_name),
                coalesce_str(self.currency.iso_currency_code_alpha),
                coalesce_num(self.currency.iso_currency_code_num))
