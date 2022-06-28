# Taxable	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from util.dictionary_util import get_attr_key, get_dic_item


class Taxable:
    # The init method or constructor
    def __init__(self, dic):
        self.taxable = None
        self.unit_of_measure = None
        if dic is not None:
            self.taxable = get_dic_item(dic, get_attr_key(dic, 'taxable'))
            self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))