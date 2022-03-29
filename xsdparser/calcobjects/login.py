from calcobjects.util import get_attr_key, get_dic_item


class Login:
    # The init method or constructor
    def __init__(self, dic):
        self.trusted_id = get_dic_item(dic, get_attr_key(dic, 'trustedid'))

    def __str__(self):
        print_str = "Trusted Id = %s" % self.trusted_id
        return print_str
