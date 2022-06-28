# Exempt	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from util.dictionary_util import get_attr_key, get_dic_item


class Exempt:
    # The init method or constructor
    def __init__(self, dic, xml_field_name):
        self.amount = None
        self.unit_of_measure = None
        if dic is not None:
            self.amount = get_dic_item(dic, get_attr_key(dic, xml_field_name))
            self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))
