# Volume	0 - 1	Decimal
# unitOfMeasure	optional	String (1 - 3)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_num, coalesce_str


class Volume:
    # The init method or constructor
    def __init__(self, dic):
        self.volume = None
        self.unit_of_measure = None
        if dic is not None:
            self.volume = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.unit_of_measure = get_dic_item(dic, get_attr_key(dic, 'unitofmeasure'))

    def __str__(self):
        print_str = "volume = %s, unit_of_measure = %s" \
                    % (self.volume, self.unit_of_measure)
        return print_str

    def to_json(self):
        return '{"Volume": %s, "unitOfMeasure": %s}' % \
               (coalesce_num(self.volume),coalesce_str(self.unit_of_measure))
