# SupplementaryUnit	0 - 1	Decimal
# unitType	optional	String (0 - 20)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_num


class SupplementaryUnit:
    # The init method or constructor
    def __init__(self, dic):
        self.supplementary_unit = None
        self.unit_type = None
        if dic is not None:
            self.supplementary_unit = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.unit_type = get_dic_item(dic, get_attr_key(dic, 'unittype'))

    def __str__(self):
        print_str = "supplementary_unit = %s, unit_type = %s" \
                    % (self.supplementary_unit, self.unit_type)
        return print_str

    def to_json(self):
        return '{"SupplementaryUnit": %s, ' \
               '"unitType": %s}' % \
               (coalesce_num(self.supplementary_unit),
                coalesce_str(self.unit_type))
