# DispatcherCode	1	String (0 - 40)
# classCode	optional	String (1 - 40)
# TaxRegistration	0 - unlimited
from calcobjects.taxregistration import TaxRegistration
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str


class Dispatcher:
    # The init method or constructor
    def __init__(self, dic):
        self.tax_registration = TaxRegistration(dic)
        self.dispatcher_code = None
        self.class_code = None
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'taxregistration') is not None:
                self.tax_registration = TaxRegistration(get_dic_item(dic, get_dic_key(dic, 'taxregistration')))
            # else:
            #     self.tax_registration = None
            # Fields
            self.dispatcher_code = get_dic_item(dic, get_attr_key(dic, 'dispatchercode'))
            self.class_code = get_dic_item(dic, get_attr_key(dic, 'classcode'))

    def __str__(self):
        print_str = "dispatcher_code = %s, class_code = %s, tax_registration = %s" \
                    % (self.dispatcher_code, self.class_code, self.tax_registration)
        return print_str

    def to_json(self):
        return '{"DispatcherCode": %s, ' \
               '"classCode": %s, ' \
               '"TaxRegistration": %s}' % \
               (coalesce_str(self.dispatcher_code),
                coalesce_str(self.class_code),
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
