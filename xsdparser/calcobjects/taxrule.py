# TaxRuleId	0 - 1	Positive Integer
# userDefined	optional	Boolean
# salesTaxHolidayIndicator	optional	Boolean
# taxRuleType	optional	TaxRuleCode

from util.dictionary_util import get_attr_key, get_dic_item, get_dic_bool_item


class TaxRule:
    # The init method or constructor
    def __init__(self, dic, xml_field_name):
        self.tax_rule_id = None
        self.user_defined = False
        self.sales_tax_holiday_indicator = False
        self.tax_rule_type = None
        if dic is not None:
            self.tax_rule_id = get_dic_item(dic, get_attr_key(dic, xml_field_name))
            self.user_defined = get_dic_bool_item(dic, get_attr_key(dic, 'userdefined'))
            self.sales_tax_holiday_indicator = get_dic_bool_item(dic, get_attr_key(dic, 'salestaxholidayindicator'))
            self.tax_rule_type = get_dic_item(dic, get_attr_key(dic, 'taxruletype'))