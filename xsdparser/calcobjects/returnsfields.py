# ReturnsDateField	0 - unlimited
# ReturnsNumericField	0 - unlimited
# ReturnsCodeField	0 - unlimited
# ReturnsIndicatorField	0 - unlimited
from calcobjects.returnscodefields import ReturnsCodeFields
from calcobjects.returnsdatefields import ReturnsDateFields
from calcobjects.returnsindicatorfields import ReturnsIndicatorFields
from calcobjects.returnsnumericfields import ReturnsNumericFields
from calcobjects.util import get_dic_item, get_dic_key


class ReturnsFields:
    # The init method or constructor
    def __init__(self, dic):
        if get_dic_key(dic, 'returnsdatefield') is not None:
            self.returns_date_fields = \
                ReturnsDateFields(get_dic_item(dic, get_dic_key(dic, 'returnsdatefield')))
        else:
            self.returns_date_fields = None
        if get_dic_key(dic, 'returnsnumericfield') is not None:
            self.returns_numeric_fields = \
                ReturnsNumericFields(get_dic_item(dic, get_dic_key(dic, 'returnsnumericfield')))
        else:
            self.returns_numeric_fields = None
        if get_dic_key(dic, 'returnsindicatorfield') is not None:
            self.returns_indicator_fields = \
                ReturnsIndicatorFields(get_dic_item(dic, get_dic_key(dic, 'returnsindicatorfield')))
        else:
            self.returns_indicator_fields = None
        if get_dic_key(dic, 'returnscodefield') is not None:
            self.returns_code_fields = \
                ReturnsCodeFields(get_dic_item(dic, get_dic_key(dic, 'returnscodefield')))
        else:
            self.returns_code_fields = None

    def __str__(self):
        print_str = "returns_date_fields = %s, returns_numeric_fields = %s, " \
                    "returns_indicator_fields = %s, returns_code_fields = %s" \
                    % (self.returns_date_fields, self.returns_numeric_fields,
                       self.returns_indicator_fields, self.returns_code_fields)
        return print_str
