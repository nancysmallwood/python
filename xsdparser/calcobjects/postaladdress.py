# StreetAddress1  0 - 1	String (1 - 100)
# StreetAddress2  0 - 1	String (1 - 100)
# City 0 - 1	String (1 - 60)
# MainDivision  0 - 1	String (1 - 60)
# SubDivision   0 - 1	String (1 - 60)
# PostalCode  0 - 1	String (1 - 20)
# Country	0 - 1	String (1 - 60)
from util.dictionary_util import get_attr_key, get_dic_item


class PostalAddress:
    # The init method or constructor
    def __init__(self, dic):
        self.street_address_1 = get_dic_item(dic, get_attr_key(dic, 'streetaddress1'))
        self.street_address_2 = get_dic_item(dic, get_attr_key(dic, 'streetaddress2'))
        self.city = get_dic_item(dic, get_attr_key(dic, 'city'))
        self.main_division = get_dic_item(dic, get_attr_key(dic, 'maindivision'))
        self.sub_division = get_dic_item(dic, get_attr_key(dic, 'subdivision'))
        self.postal_code = get_dic_item(dic, get_attr_key(dic, 'postalcode'))
        self.country = get_dic_item(dic, get_attr_key(dic, 'country'))

    def __str__(self):
        print_str = "street_address_1 = %s, street_address_2 = %s, city = %s, " \
                    "main_division = %s, sub_division = %s, postal_code = %s, country = %s" \
                    % (self.street_address_1, self.street_address_2, self.city,
                       self.main_division, self.sub_division, self.postal_code, self.country)
        return print_str


# <StreetAddress1>3137 Dixie Highway</StreetAddress1>
# <City>Erlanger</City>
# <MainDivision>KY</MainDivision>
# <PostalCode>41018</PostalCode>
# <Country>USA</Country>
# UNIT TEST -----------------------------------------------------------------
def test_postal_address():
    address_dictionary = {'StreetAddress1': '3137 Dixie Highway', 'City': 'Erlanger', 'MainDivision': 'KY',
                'PostalCode': '41018', 'Country': 'USA'}
    postal_address = PostalAddress(address_dictionary)
    try:
        assert postal_address.street_address_1 == '3137 Dixie Highway', \
            'street_address_1 assertion failed. ' 'Expected "3137 Dixie Highway"'
        assert postal_address.street_address_2 is None, 'street_address_2 assertion failed. ' 'Expected None'
        assert postal_address.city == 'Erlanger', 'city assertion failed. ' 'Expected "Erlanger"'
        assert postal_address.main_division == 'KY', 'main_division assertion failed. ' 'Expected "KY"'
        assert postal_address.sub_division is None, 'sub_division assertion failed. ' 'Expected None'
        assert postal_address.postal_code == '41018', 'postal_code assertion failed. ' 'Expected "41018"'
        assert postal_address.country == 'USA', 'country assertion failed. ' 'Expected "USA"'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_postal_address()
    finally:
        print("Test of postal_address PASSED")
