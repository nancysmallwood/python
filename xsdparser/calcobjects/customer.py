# isTaxExempt	optional	Boolean
# exemptionReasonCode	optional	String (1 - 4)
# CustomerCode	0 - 1
# classCode	optional	String (1 - 40)
# isBusinessIndicator	optional	Boolean
# Destination (Location)
# AdministrativeDestination (Location)
# ExemptionCertificate (ExemptionCertificate)
# TaxRegistration (TaxRegistration)
from calcobjects.customercode import CustomerCode
from calcobjects.exemptioncertificate import ExemptionCertificate
from calcobjects.location import Location
from calcobjects.taxregistration import TaxRegistration
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str, coalesce_bool, get_dic_bool_item


class Customer:
    # The init method or constructor
    def __init__(self, dic):
        self.destination = Location(None)
        self.administrative_destination = Location(None)
        self.exemption_certificate = ExemptionCertificate(None)
        self.tax_registration = TaxRegistration(None)
        self.customer_code = CustomerCode(None)
        self.is_tax_exempt = None
        self.exemption_reason_code = None
        self.class_code = None
        self.is_business_indicator = None
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'destination') is not None:
                self.destination = Location(get_dic_item(dic, get_dic_key(dic, 'destination')))
            if get_dic_key(dic, 'administrativedestination') is not None:
                self.administrative_destination = Location(
                    get_dic_item(dic, get_dic_key(dic, 'administrativedestination')))
            if get_dic_key(dic, 'exemptioncertificate') is not None:
                self.exemption_certificate = ExemptionCertificate(
                    get_dic_item(dic, get_dic_key(dic, 'exemptioncertificate')))
            if get_dic_key(dic, 'taxregistration') is not None:
                self.tax_registration = TaxRegistration(get_dic_item(dic, get_dic_key(dic, 'taxregistration')))
            if get_dic_key(dic, 'customercode') is not None:
                self.customer_code = CustomerCode(get_dic_item(dic, get_dic_key(dic, 'customercode')))
            # Fields
            if get_dic_bool_item(dic, get_attr_key(dic, 'istaxexempt')) is not None:
                self.is_tax_exempt = get_dic_bool_item(dic, get_attr_key(dic, 'istaxexempt'))
            self.exemption_reason_code = get_dic_item(dic, get_attr_key(dic, 'exemptionreasoncode'))
            self.class_code = get_dic_item(dic, get_attr_key(dic, 'classcode'))
            if get_dic_bool_item(dic, get_attr_key(dic, 'isbusinessindicator')) is not None:
                self.is_business_indicator = get_dic_bool_item(dic, get_attr_key(dic, 'isbusinessindicator'))

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

    def to_json(self):
        return '{"isTaxExempt": %s, ' \
               '"exemptionReasonCode": %s, ' \
               '"CustomerCode": %s, ' \
               '"classCode": %s, ' \
               '"isBusinessIndicator": %s, ' \
               '"Destination": %s, ' \
               '"AdministrativeDestination": %s, ' \
               '"ExemptionCertificate": %s, ' \
               '"TaxRegistration": %s}' % \
               (coalesce_bool(self.is_tax_exempt),
                coalesce_str(self.exemption_reason_code),
                self.customer_code.to_json(),
                coalesce_str(self.class_code),
                coalesce_bool(self.is_business_indicator),
                self.destination.to_json(),
                self.administrative_destination.to_json(),
                self.exemption_certificate.to_json(),
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
