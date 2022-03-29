# StreetAddress1  0 - 1	String (1 - 100)
# StreetAddress2  0 - 1	String (1 - 100)
# City 0 - 1	String (1 - 60)
# MainDivision  0 - 1	String (1 - 60)
# SubDivision   0 - 1	String (1 - 60)
# PostalCode  0 - 1	String (1 - 20)
# Country	0 - 1	String (1 - 60)
from calcobjects.util import get_attr_key, get_dic_item


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
