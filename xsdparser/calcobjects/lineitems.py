# lineItemNumber	optional	Long
# lineItemId	optional	String (1 - 40)
# Seller	0 - 1
# Customer	0 - 1
# Product	0 - 1
# Quantity	0 - 1
from calcobjects.lineitem import LineItem


class LineItems:
    # The init method or constructor
    def __init__(self, items):
        self.line_items = []
        if isinstance(items, list):
            for item in items:
                self.line_items.append(LineItem(item))
        elif isinstance(items, dict):
            print("dict")
        else:
            print("unknown")

    def __str__(self):
        pretty_str = ''
        for item in self.line_items:
            pretty_str += '\n %s ' % item
        return pretty_str

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
