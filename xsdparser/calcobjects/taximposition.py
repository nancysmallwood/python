# Imposition	0 - 1	String
# userDefined	optional	Boolean
# impositionId	optional	Positive Integer

from util.dictionary_util import get_attr_key, get_dic_item, get_dic_bool_item


class TaxImposition:
    # The init method or constructor
    def __init__(self, dic):
        self.imposition = None
        self.user_defined = False
        self.imposition_id = None
        if dic is not None:
            if get_dic_item(dic, get_attr_key(dic, 'text')):
                self.imposition = get_dic_item(dic, get_attr_key(dic, 'text'))
            else:
                self.imposition = get_dic_item(dic, get_attr_key(dic, 'imposition'))
            self.user_defined = get_dic_bool_item(dic, get_attr_key(dic, 'userdefined'))
            self.imposition_id = get_dic_item(dic, get_attr_key(dic, 'impositionid'))