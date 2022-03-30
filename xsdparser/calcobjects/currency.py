# isoCurrencyName  optional  String
# isoCurrencyCodeAlpha   optional  String (3)
# isoCurrencyCodeNum   optional   Positive Integer (1 - 999)
import json

from util.dictionary_util import get_dic_item, get_attr_key


class Currency:
    # The init method or constructor
    def __init__(self, dic):
        self.iso_currency_name = get_dic_item(dic, get_attr_key(dic, 'isocurrencyname'))
        self.iso_currency_code_alpha = get_dic_item(dic, get_attr_key(dic, 'isocurrencycodealpha'))
        self.iso_currency_code_num = get_dic_item(dic, get_attr_key(dic, 'isocurrencycodenum'))

    def __str__(self):
        print_str = "iso_currency_name = %s, iso_currency_code_alpha = %s, iso_currency_code_num = %s" \
                    % (self.iso_currency_name, self.iso_currency_code_alpha, self.iso_currency_code_num)
        return print_str


# UNIT TEST -----------------------------------------------------------------
def test_currency():
    json_str = json.loads('{"@isoCurrencyName":"Canadian Dollar","@isoCurrencyCodeAlpha":"CAD",'
                          '"@isoCurrencyCodeNum":124}')
    currency = Currency(json_str)
    try:
        assert currency.iso_currency_name == 'Canadian Dollar', 'iso_currency_name assertion failed. ' \
                                                                'Expected "Canadian Dollar"'
        assert currency.iso_currency_code_alpha == 'CAD', 'iso_currency_code_alpha assertion failed. ' \
                                                          'Expected "CAD"'
        assert currency.iso_currency_code_num == 124, 'iso_currency_code_num assertion failed. ' \
                                                      'Expected 124'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_currency()
    finally:
        print("Test of currency PASSED")
