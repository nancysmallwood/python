# SupplementaryUnit	0 - 1	Decimal
# unitType	optional	String (0 - 20)

from calcobjects.util import get_attr_key, get_dic_item, xml_to_dict


class SupplementaryUnit:
    # The init method or constructor
    def __init__(self, dic):
        self.supplementary_unit = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.unit_type = get_dic_item(dic, get_attr_key(dic, 'unittype'))

    def __str__(self):
        print_str = "supplementary_unit = %s, unit_type = %s" \
                    % (self.supplementary_unit, self.unit_type)
        return print_str
