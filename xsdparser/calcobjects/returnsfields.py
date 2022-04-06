# ReturnsDateField	0 - unlimited
# ReturnsNumericField	0 - unlimited
# ReturnsCodeField	0 - unlimited
# ReturnsIndicatorField	0 - unlimited
from calcobjects.returnscodefields import ReturnsCodeFields
from calcobjects.returnsdatefields import ReturnsDateFields
from calcobjects.returnsindicatorfields import ReturnsIndicatorFields
from calcobjects.returnsnumericfields import ReturnsNumericFields
from util.dictionary_util import get_dic_item, get_dic_key


class ReturnsFields:
    # The init method or constructor
    def __init__(self, dic):
        self.returns_date_fields = ReturnsDateFields(dic)
        self.returns_numeric_fields = ReturnsNumericFields(dic)
        self.returns_indicator_fields = ReturnsIndicatorFields(dic)
        self.returns_code_fields = ReturnsCodeFields(dic)
        if dic is not None:
            if get_dic_key(dic, 'returnsdatefield') is not None:
                self.returns_date_fields = \
                    ReturnsDateFields(get_dic_item(dic, get_dic_key(dic, 'returnsdatefield')))
            if get_dic_key(dic, 'returnsnumericfield') is not None:
                self.returns_numeric_fields = \
                    ReturnsNumericFields(get_dic_item(dic, get_dic_key(dic, 'returnsnumericfield')))
            if get_dic_key(dic, 'returnsindicatorfield') is not None:
                self.returns_indicator_fields = \
                    ReturnsIndicatorFields(get_dic_item(dic, get_dic_key(dic, 'returnsindicatorfield')))
            if get_dic_key(dic, 'returnscodefield') is not None:
                self.returns_code_fields = \
                    ReturnsCodeFields(get_dic_item(dic, get_dic_key(dic, 'returnscodefield')))

    def __str__(self):
        print_str = "returns_date_fields = %s, returns_numeric_fields = %s, " \
                    "returns_indicator_fields = %s, returns_code_fields = %s" \
                    % (self.returns_date_fields, self.returns_numeric_fields,
                       self.returns_indicator_fields, self.returns_code_fields)
        return print_str

    def to_json(self):
        return '{"ReturnsCodeField": %s, ' \
               '"ReturnsNumericField": %s, ' \
               '"ReturnsDateField": %s, ' \
               '"ReturnsIndicatorField": %s}' % \
               (self.returns_code_fields.to_json(),
                self.returns_numeric_fields.to_json(),
                self.returns_date_fields.to_json(),
                self.returns_indicator_fields.to_json())
