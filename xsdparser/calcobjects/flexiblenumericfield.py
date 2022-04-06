# FlexibleNumericField	0 - 10	Decimal
# fieldId	required	Integer (1 - 10)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_num


class FlexibleNumericField:
    # The init method or constructor
    def __init__(self, dic):
        self.flexible_numeric_field = None
        self.field_id = None
        if dic is not None:
            self.flexible_numeric_field = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.field_id = get_dic_item(dic, get_attr_key(dic, 'fieldid'))

    def __str__(self):
        print_str = "flexible_numeric_field = %s, field_id = %s" \
                    % (self.flexible_numeric_field, self.field_id)
        return print_str

    def to_json(self):
        return '{"id": %s, ' \
               '"value": %s}' % \
               (coalesce_num(self.field_id),
                coalesce_num(self.flexible_numeric_field))
