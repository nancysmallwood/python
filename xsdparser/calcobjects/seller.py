# nexusIndicator	optional	Boolean
# nexusReasonCode	optional	String (1 - 4)
# Company	0 - 1	String (0 - 40)
# Division	0 - 1	String (0 - 40)
# Department	0 - 1	String (0 - 40)
# UtilityProvider	0 - 1	String
# Dispatcher (Dispatcher)
# PhysicalOrigin (Location)
# AdministrativeOrigin (Location)
# TaxRegistration (TaxRegistration)
from calcobjects.location import Location
from calcobjects.dispatcher import Dispatcher
from calcobjects.taxregistration import TaxRegistration
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_bool, coalesce_str


class Seller:
    # The init method or constructor
    def __init__(self, dic):
        self.dispatcher = Dispatcher(dic)
        self.physical_origin = Location(dic)
        self.administrative_origin = Location(dic)
        self.tax_registration = TaxRegistration(dic)
        self.nexus_indicator = False
        self.nexus_reason_code = None
        self.company = None
        self.division = None
        self.department = None
        self.utility_provider = None

        if dic is not None:
            # Objects
            if get_dic_key(dic, 'dispatcher') is not None:
                self.dispatcher = Dispatcher(get_dic_item(dic, get_dic_key(dic, 'dispatcher')))
            if get_dic_key(dic, 'physicalorigin') is not None:
                self.physical_origin = Location(get_dic_item(dic, get_dic_key(dic, 'physicalorigin')))
            if get_dic_key(dic, 'administrativeorigin') is not None:
                self.administrative_origin = Location(get_dic_item(dic, get_dic_key(dic, 'administrativeorigin')))
            if get_dic_key(dic, 'administrativeorigin') is not None:
                self.tax_registration = TaxRegistration(get_dic_item(dic, get_dic_key(dic, 'taxregistration')))
            # Fields
            if get_dic_item(dic, get_attr_key(dic, 'nexusindicator')) is not None:
                self.nexus_indicator = get_dic_item(dic, get_attr_key(dic, 'nexusindicator'))
            self.nexus_reason_code = get_dic_item(dic, get_attr_key(dic, 'nexusreasoncode'))
            self.company = get_dic_item(dic, get_attr_key(dic, 'company'))
            self.division = get_dic_item(dic, get_attr_key(dic, 'division'))
            self.department = get_dic_item(dic, get_attr_key(dic, 'department'))
            self.utility_provider = get_dic_item(dic, get_attr_key(dic, 'utilityprovider'))

    def __str__(self):
        print_str = "\n\tnexus_indicator = %s, \n\tnexus_reason_code = %s, \n\tcompany = %s, " \
                    "\n\tdivision = %s, \n\tdepartment = %s, \n\tutility_provider = %s, " \
                    "\n\tdispatcher = %s, \n\tphysical_origin = %s, \n\tadministrative_origin = %s, " \
                    "\n\ttax_registration = % s " \
                    % (self.nexus_indicator, self.nexus_reason_code, self.company,
                       self.division, self.department, self.utility_provider,
                       self.dispatcher, self.physical_origin, self.administrative_origin,
                       self.tax_registration)
        return print_str

    def to_json(self):
        return '{"nexusIndicator": %s, ' \
               '"nexusReasonCode": %s, ' \
               '"Company": %s, ' \
               '"Division": %s, ' \
               '"Department": %s, ' \
               '"UtilityProvider": %s, ' \
               '"Dispatcher": %s, ' \
               '"PhysicalOrigin": %s, ' \
               '"AdministrativeOrigin": %s, ' \
               '"TaxRegistration": %s}' % \
               (coalesce_bool(self.nexus_indicator),
                coalesce_str(self.nexus_reason_code),
                coalesce_str(self.company),
                coalesce_str(self.division),
                coalesce_str(self.department),
                coalesce_str(self.utility_provider),
                self.dispatcher.to_json(),
                self.physical_origin.to_json(),
                self.administrative_origin.to_json(),
                self.tax_registration.to_json())


# # UNIT TEST -----------------------------------------------------------------
# def test_nexus_override():
#     nexus_override_dictionary = {'locationrole': 'DESTINATION',
#                                   'country': True}
#     nexus_override = NexusOverride(nexus_override_dictionary)
#     try:
#         assert nexus_override.location_role == 'DESTINATION', \
#             'nexus_override assertion failed. ' 'Expected "DESTINATION"'
#         assert nexus_override.country == True, 'country assertion failed. ' 'Expected True'
#         assert nexus_override.sub_division is None, 'subdivision assertion failed. ' \
#                                                                        'Expected None'
#     except AssertionError as msg:
#         print(msg)
#
#
# # MAIN -----------------------------------------------------------------
# # Executes unit test
# if __name__ == '__main__':
#     try:
#         test_nexus_override()
#     finally:
#         print("Test of ImpositionType PASSED")
