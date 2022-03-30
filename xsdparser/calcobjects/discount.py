# UserDefinedDiscountCode	optional
# ProratePercentage	0 - 1	Decimal
from calcobjects.userdefineddiscountcode import UserDefinedDiscountCode
from calcobjects.util import get_attr_key, get_dic_item, get_dic_key


class Discount:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'userdefineddiscountcode') is not None:
            self.user_defined_discount_code = \
                UserDefinedDiscountCode(get_dic_item(dic, get_dic_key(dic, 'userdefineddiscountcode')))
        else:
            self.user_defined_discount_code = None
        # Fields
        self.prorate_percentage = get_dic_item(dic, get_attr_key(dic, 'proratepercentage'))

    def __str__(self):
        print_str = "user_defined_discount_code=%s, prorate_percentage= %s" % \
                    (self.user_defined_discount_code, self.prorate_percentage)
        return print_str
