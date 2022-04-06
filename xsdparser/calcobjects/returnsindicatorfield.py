# ReturnsIndicatorField	0 - unlimited	Boolean
# name	required	String

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_bool


class ReturnsIndicatorField:
    # The init method or constructor
    def __init__(self, dic):
        self.returns_indicator_field = False
        self.name = None
        if dic is not None:
            if get_dic_item(dic, get_attr_key(dic, 'text')) is not None:
                self.returns_indicator_field = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.name = get_dic_item(dic, get_attr_key(dic, 'name'))

    def __str__(self):
        print_str = "returns_indicator_field = %s, name = %s" \
                    % (self.returns_indicator_field, self.name)
        return print_str

    def to_json(self):
        return '{"name": %s, ' \
               '"value": %s}' % \
               (coalesce_str(self.name),
                coalesce_bool(self.returns_indicator_field))
