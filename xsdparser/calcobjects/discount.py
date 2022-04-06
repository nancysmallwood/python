# UserDefinedDiscountCode	optional
# ProratePercentage	0 - 1	Decimal
from calcobjects.userdefineddiscountcode import UserDefinedDiscountCode
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str, coalesce_num


class Discount:
    # The init method or constructor
    def __init__(self, dic):
        # self.user_defined_discount_code = UserDefinedDiscountCode(dic)
        self.user_defined_discount_code = None
        self.discount_percent = None
        self.discount_amount = None
        self.prorate_percentage = None
        if dic is not None:
            # Objects
            # if get_dic_key(dic, 'userdefineddiscountcode') is not None:
            #     self.user_defined_discount_code = \
            #         UserDefinedDiscountCode(get_dic_item(dic, get_dic_key(dic, 'userdefineddiscountcode')))
            # else:
            #     self.user_defined_discount_code = None
            # Fields
            self.prorate_percentage = get_dic_item(dic, get_attr_key(dic, 'proratepercentage'))
            self.user_defined_discount_code = get_dic_item(dic, get_attr_key(dic, 'userdefineddiscountcode'))
            self.discount_percent = get_dic_item(dic, get_attr_key(dic, 'discountpercent'))
            self.discount_amount = get_dic_item(dic, get_attr_key(dic, 'discountamount'))

    def __str__(self):
        print_str = "user_defined_discount_code=%s, prorate_percentage= %s, " \
                    "discount_percent = %s, discount_amount = %s" % \
                    (self.user_defined_discount_code, self.prorate_percentage,
                     self.discount_percent, self.discount_amount)
        return print_str

    def to_json(self):
        return '{"userDefinedDiscountCode": %s, ' \
               '"ProratePercentage": %s, ' \
               '"DiscountPercent": %s, ' \
               '"DiscountAmount": %s}' % \
               (coalesce_str(self.user_defined_discount_code),
                coalesce_num(self.prorate_percentage),
                coalesce_num(self.discount_percent),
                coalesce_num(self.discount_amount))