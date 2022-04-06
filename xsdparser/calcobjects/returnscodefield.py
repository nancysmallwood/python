# ReturnsCodeField	0 - unlimited	String
# name	required	String

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str


class ReturnsCodeField:
    # The init method or constructor
    def __init__(self, dic):
        self.returns_code_field = None
        self.name = None
        if dic is not None:
            self.returns_code_field = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.name = get_dic_item(dic, get_attr_key(dic, 'name'))

    def __str__(self):
        print_str = "returns_code_field = %s, name = %s" \
                    % (self.returns_code_field, self.name)
        return print_str

    def to_json(self):
        return '{"name": %s, ' \
               '"value": %s}' % \
               (coalesce_str(self.name),
                coalesce_str(self.returns_code_field))
