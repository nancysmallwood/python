# locationRole	required	TaxingLocationCode
# country	optional	Boolean
# mainDivision	optional	Boolean
# subDivision	optional	Boolean
# city	optional	Boolean
# district	optional	Boolean
from util.dictionary_util import get_attr_key, get_dic_item, coalesce_str, coalesce_bool


class NexusOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.location_role = None
        self.country = False
        self.main_division = False
        self.sub_division = False
        self.city = False
        self.district = False

        if dic is not None:
            self.location_role = get_dic_item(dic, get_attr_key(dic, 'locationrole'))
            if get_dic_item(dic, get_attr_key(dic, 'country')) is not None:
                self.country = get_dic_item(dic, get_attr_key(dic, 'country'))
            if get_dic_item(dic, get_attr_key(dic, 'maindivision')) is not None:
                self.main_division = get_dic_item(dic, get_attr_key(dic, 'maindivision'))
            if get_dic_item(dic, get_attr_key(dic, 'subdivision')) is not None:
                self.sub_division = get_dic_item(dic, get_attr_key(dic, 'subdivision'))
            if get_dic_item(dic, get_attr_key(dic, 'city')) is not None:
                self.city = get_dic_item(dic, get_attr_key(dic, 'city'))
            if get_dic_item(dic, get_attr_key(dic, 'district')) is not None:
                self.district = get_dic_item(dic, get_attr_key(dic, 'district'))

    def __str__(self):
        print_str = "location_role = %s, country = %s, main_division = %s" \
                    "sub_division = %s, city = %s, district = %s" \
                    % (self.location_role, self.country, self.main_division,
                       self.sub_division, self.city, self.district)
        return print_str

    def to_json(self):
        return '{"locationRole": %s, ' \
               '"country": %s, ' \
               '"mainDivision": %s, ' \
               '"subDivision": %s, ' \
               '"city": %s, ' \
               '"district": %s}' % \
               (coalesce_str(self.location_role),
                coalesce_bool(self.country),
                coalesce_bool(self.main_division),
                coalesce_bool(self.sub_division),
                coalesce_bool(self.city),
                coalesce_bool(self.district))


# UNIT TEST -----------------------------------------------------------------
def test_nexus_override():
    nexus_override_dictionary = {'locationrole': 'DESTINATION',
                                  'country': True}
    nexus_override = NexusOverride(nexus_override_dictionary)
    try:
        assert nexus_override.location_role == 'DESTINATION', \
            'nexus_override assertion failed. ' 'Expected "DESTINATION"'
        assert nexus_override.country == True, 'country assertion failed. ' 'Expected True'
        assert nexus_override.sub_division is None, 'subdivision assertion failed. ' \
                                                                       'Expected None'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_nexus_override()
    finally:
        print("Test of ImpositionType PASSED")
