# CustomerCode	0 - 1
# classCode	optional	String (1 - 40)
# isBusinessIndicator	optional	Boolean

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_bool


class CustomerCode:
    # The init method or constructor
    def __init__(self, dic):
        self.customer_code = None
        self.class_code = None
        self.is_business_indicator = False
        if dic is not None:
            self.customer_code = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.class_code = get_dic_item(dic, get_attr_key(dic, 'classcode'))
            if get_dic_item(dic, get_attr_key(dic, 'isbusinessindicator')) is not None:
                self.is_business_indicator = get_dic_item(dic, get_attr_key(dic, 'isbusinessindicator'))

    def __str__(self):
        print_str = "CustomerCode = %s, class_code = %s, is_business_indicator = %s" \
                    % (self.customer_code, self.class_code, self.is_business_indicator)
        return print_str

    def to_json(self):
        return '{"CustomerCode": %s, ' \
               '"classCode": %s, ' \
               '"isBusinessIndicator": %s}' % \
               (coalesce_str(self.customer_code),
                coalesce_str(self.class_code),
                coalesce_bool(self.is_business_indicator))