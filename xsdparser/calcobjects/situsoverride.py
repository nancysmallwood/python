# taxingLocation	required	TaxingLocationCode

from calcobjects.util import get_attr_key, get_dic_item


class SitusOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.taxing_location = get_dic_item(dic, get_attr_key(dic, 'taxinglocation'))

    def __str__(self):
        print_str = "taxing_location=%s" % self.taxing_location
        return print_str
