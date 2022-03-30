# FlexibleCodeField	0 - 25
# FlexibleNumericField	0 - 10
# FlexibleDateField	0 - 5
from calcobjects.flexiblecodefields import FlexibleCodeFields
from calcobjects.flexibledatefields import FlexibleDateFields
from calcobjects.flexiblenumericfields import FlexibleNumericFields
from util.dictionary_util import get_dic_item, get_dic_key


class FlexibleFields:
    # The init method or constructor
    def __init__(self, dic):
        if get_dic_key(dic, 'flexiblecodefield') is not None:
            self.flexible_code_fields = \
                FlexibleCodeFields(get_dic_item(dic, get_dic_key(dic, 'flexiblecodefield')))
        else:
            self.flexible_code_fields = None
        if get_dic_key(dic, 'flexiblenumericfield') is not None:
            self.flexible_numeric_fields = \
                FlexibleNumericFields(get_dic_item(dic, get_dic_key(dic, 'flexiblenumericfield')))
        else:
            self.flexible_numeric_fields = None
        if get_dic_key(dic, 'flexibledatefield') is not None:
            self.flexible_date_fields = \
                FlexibleDateFields(get_dic_item(dic, get_dic_key(dic, 'flexibledatefield')))
        else:
            self.flexible_date_fields = None

    def __str__(self):
        print_str = "flexible_code_fields = %s, flexible_numeric_fields = %s, flexible_date_fields = %s" \
                    % (self.flexible_code_fields, self.flexible_numeric_fields, self.flexible_date_fields)
        return print_str
