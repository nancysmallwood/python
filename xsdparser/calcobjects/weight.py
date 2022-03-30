# Weight	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from calcobjects.util import get_attr_key, get_dic_item, xml_to_dict


class Weight:
    # The init method or constructor
    def __init__(self, dic):
        self.weight = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))

    def __str__(self):
        print_str = "weight = %s, unit_of_measure = %s" \
                    % (self.weight, self.unit_of_measure)
        return print_str