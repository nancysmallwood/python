from util.dictionary_util import get_attr_key, get_dic_item


class Login:
    # The init method or constructor
    def __init__(self, dic):
        self.trusted_id = get_dic_item(dic, get_attr_key(dic, 'trustedid'))
        self.user_name = get_dic_item(dic, get_attr_key(dic, 'username'))

    def __str__(self):
        print_str = "Trusted Id = %s, User Name = %s" % (self.trusted_id, self.user_name)
        return print_str
