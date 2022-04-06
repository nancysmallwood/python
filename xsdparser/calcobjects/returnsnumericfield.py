# ReturnsNumericField	0 - unlimited	Decimal
# name	required	String

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_num


class ReturnsNumericField:
    # The init method or constructor
    def __init__(self, dic):
        self.returns_numeric_field = None
        self.name = None
        if dic is not None:
            self.returns_numeric_field = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.name = get_dic_item(dic, get_attr_key(dic, 'name'))

    def __str__(self):
        print_str = "returns_numeric_field = %s, name = %s" \
                    % (self.returns_numeric_field, self.name)
        return print_str

    def to_json(self):
        return '{"name": %s, ' \
               '"value": %s}' % \
               (coalesce_str(self.name),
                coalesce_num(self.returns_numeric_field))
