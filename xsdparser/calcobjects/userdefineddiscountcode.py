# userDefinedDiscountCode	optional	String (0 - 20)
# DiscountPercent*	1	Decimal
# DiscountAmount*	1	Decimal

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_num


class UserDefinedDiscountCode:
    # The init method or constructor
    def __init__(self, dic):
        self.user_defined_discount_code = None
        self.discount_percent = None
        self.discount_amount = None
        if dic is not None:
            self.user_defined_discount_code = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.discount_percent = get_dic_item(dic, get_attr_key(dic, 'discountpercent'))
            self.discount_amount = get_dic_item(dic, get_attr_key(dic, 'discountamount'))

    def __str__(self):
        print_str = "user_defined_discount_code=%s, discount_percent= %s, discount_amount= %s" % \
                    (self.user_defined_discount_code, self.discount_percent, self.discount_amount)
        return print_str

    def to_json(self):
        return '{"userDefinedDiscountCode": %s, ' \
               '"DiscountPercent": %s, ' \
               '"DiscountAmount": %s}' % \
               (coalesce_str(self.user_defined_discount_code),
                coalesce_num(self.discount_percent),
                coalesce_num(self.discount_amount))
