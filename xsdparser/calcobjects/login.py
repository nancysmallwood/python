from util.dictionary_util import get_attr_key, get_dic_item, null, coalesce_str


class Login:
    # The init method or constructor
    def __init__(self, dic):
        self.trusted_id = None
        self.user_name = None
        if dic is not None:
            if get_attr_key(dic, 'trustedid') is not None:
                self.trusted_id = get_dic_item(dic, get_attr_key(dic, 'trustedid'))
            if get_attr_key(dic, 'username') is not None:
                self.user_name = get_dic_item(dic, get_attr_key(dic, 'username'))

    def __str__(self):
        print_str = "Trusted Id = %s, User Name = %s" % (self.trusted_id, self.user_name)
        return print_str

    def to_json(self):
        return '{"UserName": %s, "TrustedId": %s}' % \
               (coalesce_str(self.user_name),coalesce_str(self.trusted_id))


