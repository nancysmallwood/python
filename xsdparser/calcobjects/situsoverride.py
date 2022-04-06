# taxingLocation	required	TaxingLocationCode

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str


class SitusOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.taxing_location = None
        if dic is not None:
            self.taxing_location = get_dic_item(dic, get_attr_key(dic, 'taxinglocation'))

    def __str__(self):
        print_str = "taxing_location=%s" % self.taxing_location
        return print_str

    def to_json(self):
        return '{"taxingLocation": %s}' % \
               (coalesce_str(self.taxing_location))

