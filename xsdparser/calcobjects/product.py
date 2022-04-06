# text 0 - 1	String (0 - 40)
# productClass	optional	String (0 - 40)

from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str


class Product:
    # The init method or constructor
    def __init__(self, dic):
        self.product = None
        self.product_class = None
        if dic is not None:
            self.product = get_dic_item(dic, get_attr_key(dic, 'text'))
            self.product_class = get_dic_item(dic, get_attr_key(dic, 'productclass'))

    def __str__(self):
        print_str = "product=%s, product_class= %s" % (self.product, self.product_class)
        return print_str

    def to_json(self):
        return '{"Product": %s, ' \
               '"productClass": %s}' % \
               (coalesce_str(self.product),
                coalesce_str(self.product_class))

