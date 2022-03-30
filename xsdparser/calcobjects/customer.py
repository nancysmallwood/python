# isTaxExempt	optional	Boolean
# exemptionReasonCode	optional	String (1 - 4)
# CustomerCode	0 - 1
# classCode	optional	String (1 - 40)
# isBusinessIndicator	optional	Boolean
# Destination (Location)
# AdministrativeDestination (Location)
# ExemptionCertificate (ExemptionCertificate)
# TaxRegistration (TaxRegistration)
from calcobjects.exemptioncertificate import ExemptionCertificate
from calcobjects.location import Location
from calcobjects.taxregistration import TaxRegistration
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key


class Customer:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'destination') is not None:
            self.destination = Location(get_dic_item(dic, get_dic_key(dic, 'destination')))
        else:
            self.destination = None
        if get_dic_key(dic, 'administrativedestination') is not None:
            self.administrative_destination = Location(get_dic_item(dic, get_dic_key(dic, 'administrativedestination')))
        else:
            self.administrative_destination = None
        if get_dic_key(dic, 'exemptioncertificate') is not None:
            self.exemption_certificate = ExemptionCertificate(get_dic_item(dic, get_dic_key(dic, 'exemptioncertificate')))
        else:
            self.exemption_certificate = None
        if get_dic_key(dic, 'taxregistration') is not None:
            self.tax_registration = TaxRegistration(get_dic_item(dic, get_dic_key(dic, 'taxregistration')))
        else:
            self.tax_registration = None
        # Fields
        self.is_tax_exempt = get_dic_item(dic, get_attr_key(dic, 'istaxexempt'))
        self.exemption_reason_code = get_dic_item(dic, get_attr_key(dic, 'exemptionreasoncode'))
        self.customer_code = get_dic_item(dic, get_attr_key(dic, 'customercode'))
        self.class_code = get_dic_item(dic, get_attr_key(dic, 'classcode'))
        self.is_business_indicator = get_dic_item(dic, get_attr_key(dic, 'isbusinessindicator'))


    def __str__(self):
        print_str = "\n\tis_tax_exempt = %s, \n\texemption_reason_code = %s, \n\tcustomer_code = %s, " \
                    "\n\tclass_code = %s, \n\tis_business_indicator = %s, \n\tdestination = %s, " \
                    "\n\tadministrative_destination = %s, \n\texemption_certificate = %s, " \
                    "\n\ttax_registration = %s " \
                    % (self.is_tax_exempt, self.exemption_reason_code, self.customer_code,
                       self.class_code, self.is_business_indicator, self.destination,
                       self.administrative_destination, self.exemption_certificate,
                       self.tax_registration)
        return print_str


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
