# FlexibleDateField	0 - 5	Date (yyyy-mm-dd)
# fieldId	required	Integer (1 - 5)

from calcobjects.util import get_attr_key, get_dic_item


class FlexibleDateField:
    # The init method or constructor
    def __init__(self, dic):
        self.flexible_date_field = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.field_id = get_dic_item(dic, get_attr_key(dic, 'fieldid'))

    def __str__(self):
        print_str = "flexible_date_field = %s, field_id = %s" \
                    % (self.flexible_date_field, self.field_id)
        return print_str
