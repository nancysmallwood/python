# text	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_num


class Quantity:
    # The init method or constructor
    def __init__(self, dic):
        self.quantity = None
        self.unit_of_measure = None
        if dic is not None:
            self.quantity = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))

    def __str__(self):
        print_str = "quantity= %s, unit_of_measure=%s" % (self.quantity, self.unit_of_measure)
        return print_str

    def to_json(self):
        return '{"Quantity": %s, "unitOfMeasure": %s}' % \
               (coalesce_num(self.quantity),coalesce_str(self.unit_of_measure))

