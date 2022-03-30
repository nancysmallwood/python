# lineItemNumber	optional	Long
# lineItemId	optional	String (1 - 40)
# Seller	0 - 1
# Customer	0 - 1
# Product	0 - 1
# Quantity	0 - 1
from calcobjects.customer import Customer
from calcobjects.product import Product
from calcobjects.quantity import Quantity
from calcobjects.seller import Seller
from calcobjects.util import get_attr_key, get_dic_item, xml_to_dict, get_dic_key


class LineItem:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'seller') is not None:
            self.seller = Seller(get_dic_item(dic, get_dic_key(dic, 'seller')))
        else:
            self.seller = None
        if get_dic_key(dic, 'customer') is not None:
            self.customer = Customer(get_dic_item(dic, get_dic_key(dic, 'customer')))
        else:
            self.customer = None
        if get_dic_key(dic, 'product') is not None:
            self.product = Product(get_dic_item(dic, get_dic_key(dic, 'product')))
        else:
            self.product = None
        if get_dic_key(dic, 'quantity') is not None:
            self.quantity = Quantity(get_dic_item(dic, get_dic_key(dic, 'quantity')))
        else:
            self.quantity = None
        self.line_item_number = get_dic_item(dic, get_attr_key(dic, 'lineitemnumber'))
        self.line_item_id = get_dic_item(dic, get_attr_key(dic, 'lineitemid'))

    def __str__(self):
        print_str = "\nline_item_number = %s, \nline_item_id = %s, \nseller = %s, " \
                    "\ncustomer = %s, \nproduct = %s, \nquantity = %s" \
                    % (self.line_item_number, self.line_item_id, self.seller,
                       self.customer, self.product, self.quantity)
        return print_str


# <StreetAddress1>3137 Dixie Highway</StreetAddress1>
# <City>Erlanger</City>
# <MainDivision>KY</MainDivision>
# <PostalCode>41018</PostalCode>
# <Country>USA</Country>
# UNIT TEST -----------------------------------------------------------------
# def test_postal_address():
#     address_dictionary = {'StreetAddress1': '3137 Dixie Highway', 'City': 'Erlanger', 'MainDivision': 'KY',
#                 'PostalCode': '41018', 'Country': 'USA'}
#     postal_address = PostalAddress(address_dictionary)
#     try:
#         assert postal_address.street_address_1 == '3137 Dixie Highway', \
#             'street_address_1 assertion failed. ' 'Expected "3137 Dixie Highway"'
#         assert postal_address.street_address_2 is None, 'street_address_2 assertion failed. ' 'Expected None'
#         assert postal_address.city == 'Erlanger', 'city assertion failed. ' 'Expected "Erlanger"'
#         assert postal_address.main_division == 'KY', 'main_division assertion failed. ' 'Expected "KY"'
#         assert postal_address.sub_division is None, 'sub_division assertion failed. ' 'Expected None'
#         assert postal_address.postal_code == '41018', 'postal_code assertion failed. ' 'Expected "41018"'
#         assert postal_address.country == 'USA', 'country assertion failed. ' 'Expected "USA"'
#     except AssertionError as msg:
#         print(msg)
#
#
# # MAIN -----------------------------------------------------------------
# # Executes unit test
# if __name__ == '__main__':
#     try:
#         test_postal_address()
#     finally:
#         print("Test of postal_address PASSED")
