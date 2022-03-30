# text	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from util.dictionary_util import get_attr_key, get_dic_item


class Quantity:
    # The init method or constructor
    def __init__(self, dic):
        self.quantity = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))

    def __str__(self):
        print_str = "quantity= %s, unit_of_measure=%s" % (self.quantity, self.unit_of_measure)
        return print_str
