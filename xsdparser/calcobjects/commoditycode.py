# CommodityCode	0 - 1	String (0 - 40)
# commodityCodeType	required	String (1 - 60)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str


class CommodityCode:
    # The init method or constructor
    def __init__(self, dic):
        self.commodity_code = None
        self.commodity_code_type = None
        if dic is not None:
            self.commodity_code = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.commodity_code_type = get_dic_item(dic, get_attr_key(dic, 'commoditycodetype'))

    def __str__(self):
        print_str = "commodity_code = %s, commodity_code_type = %s" \
                    % (self.commodity_code, self.commodity_code_type)
        return print_str

    def to_json(self):
        return '{"CommodityCode": %s, "commodityCodeType": %s}' % \
               (coalesce_str(self.commodity_code),coalesce_str(self.commodity_code_type))
