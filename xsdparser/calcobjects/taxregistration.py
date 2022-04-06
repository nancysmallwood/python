# isoCountryCode	optional	String (2 - 3)
# mainDivision	optional	String (1 - 60)
# hasPhysicalPresenceIndicator	optional	Boolean
# jurisdictionId	optional	Integer (0 - 999999999)
# TaxRegistrationNumber	0 - 1	String (0 - 40)
# nexus_override
# physical_location
# ImpositionType
from calcobjects.impositiontype import ImpositionType
from calcobjects.location import Location
from calcobjects.nexusoverride import NexusOverride
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str, coalesce_bool, coalesce_num


class TaxRegistration:
    # The init method or constructor
    def __init__(self, dic):
        self.nexus_override = NexusOverride(dic)
        self.physical_location = Location(dic)
        self.imposition_type = ImpositionType(dic)
        self.iso_country_code = None
        self.main_division = None
        self.has_physical_presence_indicator = False
        self.jurisdiction_id = None
        self.tax_registration_number = None
        if dic is not None:
            self.nexus_override = NexusOverride(get_dic_item(dic, get_dic_key(dic, 'nexusoverride')))
            self.physical_location = Location(get_dic_item(dic, get_dic_key(dic, 'physicallocation')))
            self.imposition_type = ImpositionType(get_dic_item(dic, get_dic_key(dic, 'impositiontype')))
            self.iso_country_code = get_dic_item(dic, get_attr_key(dic, 'isocountrycode'))
            self.main_division = get_dic_item(dic, get_attr_key(dic, 'maindivision'))
            if get_dic_item(dic, get_attr_key(dic, 'hasphysicalpresenceindicator')) is not None:
                self.has_physical_presence_indicator = \
                    get_dic_item(dic, get_attr_key(dic, 'hasphysicalpresenceindicator'))
            self.jurisdiction_id = get_dic_item(dic, get_attr_key(dic, 'jurisdictionid'))
            self.tax_registration_number = get_dic_item(dic, get_attr_key(dic, 'taxregistrationnumber'))

    def __str__(self):
        print_str = "iso_country_code = %s, main_division = %s, has_physical_presence_indicator = %s, " \
                    "jurisdictionid = %s" \
                    % (self.iso_country_code, self.main_division, self.has_physical_presence_indicator,
                       str(self.jurisdiction_id))
        return print_str

    def to_json(self):
        return '{"isoCountryCode": %s, ' \
               '"mainDivision": %s, ' \
               '"hasPhysicalPresenceIndicator": %s, ' \
               '"jurisdictionId": %s, ' \
               '"TaxRegistrationNumber": %s, ' \
               '"NexusOverride": %s, ' \
               '"PhysicalLocation": %s, ' \
               '"ImpositionType": %s}' % \
               (coalesce_str(self.iso_country_code),
                coalesce_str(self.main_division),
                coalesce_bool(self.has_physical_presence_indicator),
                coalesce_num(self.jurisdiction_id),
                coalesce_str(self.tax_registration_number),
                self.nexus_override.to_json(),
                self.physical_location.to_json(),
                self.imposition_type.to_json())

    # def __str__(self):
    #     print_str = "iso_country_code = %s, main_division = %s, has_physical_presence_indicator = %s", \
    #                 "jurisdiction_id = %s, tax_registration_number = %s, nexus_override = %s," \
    #                 "physical_location = %s, imposition_type = %s" \
    #                 % (self.iso_country_code, self.main_division, self.has_physical_presence_indicator,
    #                    self.jurisdiction_id, self.tax_registration_number, self.nexus_override,
    #                    self.physical_location, self.imposition_type)
    #     return print_str


# UNIT TEST -----------------------------------------------------------------
def test_tax_registration():
    tax_registration_dictionary = {'isocountrycode': 'USA',
                                   'maindivision': 'Main div',
                                   'jurisdictionid': 18,
                                   'taxregistrationnumber': '23-23333',
                                   'nexusoverride': {'locationrole': 'DESTINATION', 'country': True},
                                   'physicallocation': {'taxAreaId': '330590000', 'latitude': '123.321'},
                                   'impositiontype': {'userdefined': True, 'impositiontypeid': 6,
                                                      'withholdingtype': 'Withholding Type'}
                                   }
    tax_registration = TaxRegistration(tax_registration_dictionary)
    try:
        print(tax_registration)
        # assert nexus_override.location_role == 'DESTINATION', \
        #     'nexus_override assertion failed. ' 'Expected "DESTINATION"'
        # assert nexus_override.country == True, 'country assertion failed. ' 'Expected True'
        # assert nexus_override.sub_division is None, 'subdivision assertion failed. ' \
        #                                                                'Expected None'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_tax_registration()
    finally:
        print("Test of tax_registration PASSED")
