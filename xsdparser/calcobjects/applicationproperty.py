# ApplicationProperty	0 - unlimited
# key	optional

from util.dictionary_util import get_attr_key, get_dic_item, null, coalesce_str


class ApplicationProperty:
    # The init method or constructor
    def __init__(self, dic):
        self.application_property = None
        self.key = None
        if dic is not None:
            self.application_property = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.key = get_dic_item(dic, get_attr_key(dic, 'key'))

    def __str__(self):
        print_str = "application_property=%s, key= %s" % (self.application_property, self.key)
        return print_str

    def to_json(self):
        return '{"ApplicationProperty": %s, ' \
               '"Key": %s}' % \
               (coalesce_str(self.application_property),
                coalesce_str(self.key))

