# ApplicationProperty	0 - unlimited
# key	optional

from util.dictionary_util import get_attr_key, get_dic_item


class ApplicationProperty:
    # The init method or constructor
    def __init__(self, dic):
        self.application_property = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.key = get_dic_item(dic, get_attr_key(dic, 'key'))

    def __str__(self):
        print_str = "application_property=%s, key= %s" % (self.application_property, self.key)
        return print_str