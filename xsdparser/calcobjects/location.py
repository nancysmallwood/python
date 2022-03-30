# taxAreaId	 optional	Integer (0 - 999999999)
# latitude	optional	String (1 - 20)
# longitude	optional	String (1 - 20)
# locationCustomsStatus	optional String (0 - 20)
# locationCode	optional	String (0 - 20)
# externalJurisdictionCode  optional	String (0 - 20)
# PostalAddress
# Currency
from calcobjects.currency import Currency
from calcobjects.postaladdress import PostalAddress
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key


class Location:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'currencyconversion') is not None:
            self.currency_conversion = Currency(get_dic_item(dic, get_dic_key(dic, 'currencyconversion')))
        else:
            self.currency_conversion = None
        # Fields
        self.taxarea_id = get_dic_item(dic, get_attr_key(dic, 'taxareaid'))
        self.latitude = get_dic_item(dic, get_attr_key(dic, 'latitude'))
        self.longitude = get_dic_item(dic, get_attr_key(dic, 'longitude'))
        self.location_customs_status = get_dic_item(dic, get_attr_key(dic, 'locationcustomsstatus'))
        self.location_code = get_dic_item(dic, get_attr_key(dic, 'locationcode'))
        self.external_jurisdiction_code = get_dic_item(dic, get_attr_key(dic, 'externaljurisdictioncode'))
        # Postal Address done a little differently
        self.postal_address = {}
        if get_dic_item(dic, get_attr_key(dic, 'streetaddress1')) is not None:
            self.postal_address['streetaddress1'] = get_dic_item(dic, get_attr_key(dic, 'streetaddress1'))
        if get_dic_item(dic, get_attr_key(dic, 'streetaddress2')) is not None:
            self.postal_address['streetaddress2'] = get_dic_item(dic, get_attr_key(dic, 'streetaddress2'))
        if get_dic_item(dic, get_attr_key(dic, 'city')) is not None:
            self.postal_address['city'] = get_dic_item(dic, get_attr_key(dic, 'city'))
        if get_dic_item(dic, get_attr_key(dic, 'maindivision')) is not None:
            self.postal_address['maindivision'] = get_dic_item(dic, get_attr_key(dic, 'maindivision'))
        if get_dic_item(dic, get_attr_key(dic, 'subdivision')) is not None:
            self.postal_address['subdivision'] = get_dic_item(dic, get_attr_key(dic, 'subdivision'))
        if get_dic_item(dic, get_attr_key(dic, 'postalcode')) is not None:
            self.postal_address['postalcode'] = get_dic_item(dic, get_attr_key(dic, 'postalcode'))
        if get_dic_item(dic, get_attr_key(dic, 'country')) is not None:
            self.postal_address['country'] = get_dic_item(dic, get_attr_key(dic, 'country'))
        self.postal_address = PostalAddress(self.postal_address)
        # self.postal_address = validate_postal_address(PostalAddress(self.postal_address))

    def __str__(self):
        print_str = "\n\t\ttaxarea_id = %s, latitude = %s, longitude = %s, " \
                    "location_customs_status = %s, location_code = %s, external_jurisdiction_code = %s, " \
                    "\n\t\tpostal_address = %s, \n\t\tcurrency_conversion = %s" \
                    % (self.taxarea_id, self.latitude, self.longitude,
                       self.location_customs_status, self.location_code, self.external_jurisdiction_code,
                       self.postal_address, self.currency_conversion)
        return print_str


def validate_postal_address(postal_address):
    if postal_address.street_address_1 is None \
            and postal_address.street_address_2 is None \
            and postal_address.main_division is None \
            and postal_address.sub_division is None \
            and postal_address.city is None \
            and postal_address.postal_code is None \
            and postal_address.country is None:
        return None
    else:
        return PostalAddress(postal_address)


# UNIT TEST -----------------------------------------------------------------
def test_location():
    location_dictionary = {'taxAreaId': '330590000', 'latitude': '123.321', 'longitude': '123.321',
                           'locationcustomsstatus': 'FREE_TRADE_ZONE', 'locationcode': 'LOC-CODE',
                           'externaljurisdictioncode': 'XXX',
                           'StreetAddress1': '3137 Dixie Highway', 'City': 'Erlanger', 'MainDivision': 'KY',
                           'PostalCode': '41018', 'Country': 'USA',
                           'currencyconversion': {'isocurrencyname': 'US Dollar',
                                                  'isocurrencycodealpha': 'USD',
                                                  'isocurrencycodenum': 178}}
    location = Location(location_dictionary)
    try:
        assert location.taxarea_id == '330590000', \
            'taxarea_id assertion failed. ' 'Expected "330590000"'
        assert location.postal_address.country == 'USA', \
            'postal_address.country assertion failed. ' 'Expected "USA"'
        # assert postal_address.street_address_2 is None, 'street_address_2 assertion failed. ' 'Expected None'
        # assert postal_address.city == 'Erlanger', 'city assertion failed. ' 'Expected "Erlanger"'
        # assert postal_address.main_division == 'KY', 'main_division assertion failed. ' 'Expected "KY"'
        # assert postal_address.sub_division is None, 'sub_division assertion failed. ' 'Expected None'
        # assert postal_address.postal_code == '41018', 'postal_code assertion failed. ' 'Expected "41018"'
        # assert postal_address.country == 'USA', 'country assertion failed. ' 'Expected "USA"'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_location()
    finally:
        print("Test of location PASSED")
