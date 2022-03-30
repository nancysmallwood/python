# exemptionCertificateNumber  optional  String (1 - 30)

from util.dictionary_util import get_dic_item, get_attr_key


class ExemptionCertificate:
    # The init method or constructor
    def __init__(self, dic):
        self.exemption_certificate_number = get_dic_item(dic, get_attr_key(dic, 'exemptioncertificatenumber'))

    def __str__(self):
        print_str = "exemption_certificate_number = %s" \
                    % (self.exemption_certificate_number)
        return print_str


# UNIT TEST -----------------------------------------------------------------
def test_exemption_certificate():
    exemption_certificate_dictionary = {'exemptioncertificatenumber': '1234-4332'}
    exemption_certificate = ExemptionCertificate(exemption_certificate_dictionary)
    try:
        assert exemption_certificate.exemption_certificate_number == '1234-4332', \
            'exemption_certificate_number assertion failed. ' 'Expected "1234-4332"'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_exemption_certificate()
    finally:
        print("Test of ExemptionCertificate PASSED")
