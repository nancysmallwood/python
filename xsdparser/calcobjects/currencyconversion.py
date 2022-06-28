# CurrencyConversion	0 - 1	Decimal
# Currency
from calcobjects.currency import Currency
from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_num, get_dic_key


class CurrencyConversion:
    # The init method or constructor
    def __init__(self, dic):
        self.currency_conversion = None
        self.currency = Currency(dic)
        if dic is not None:
            self.currency_conversion = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.currency.iso_currency_name = get_dic_key(dic, 'isoCurrencyName')
            self.currency.iso_currency_code_alpha = get_dic_key(dic, 'isoCurrencyCodeAlpha')
            self.currency.iso_currency_code_num = get_dic_key(dic, 'isoCurrencyCodeNum')

    def __str__(self):
        print_str = "currency_conversion= %s, " \
                    "iso_currency_name=%s, " \
                    "iso_currency_code_alpha=%s, " \
                    "iso_currency_code_num=%s" % \
                    (self.currency_conversion,
                     self.currency.iso_currency_name,
                     self.currency.iso_currency_code_alpha,
                     self.currency.iso_currency_code_num)
        return print_str

    def to_json(self):
        return '{"CurrencyConversion": %s, ' \
               '"isoCurrencyName": %s, ' \
               '"isoCurrencyCodeAlpha": %s, ' \
               '"isoCurrencyCodeNum": %s}' % \
               (coalesce_num(self.currency_conversion),
                coalesce_str(self.currency.iso_currency_name),
                coalesce_str(self.currency.iso_currency_code_alpha),
                coalesce_num(self.currency.iso_currency_code_num))

