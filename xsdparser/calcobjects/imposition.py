# JurisdictionLevel	1	JurisdictionLevelCode string
# ImpositionType	0 - 1
from calcobjects.impositiontype import ImpositionType
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key


class Imposition:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'impositiontype') is not None:
            self.imposition_type = ImpositionType(get_dic_item(dic, get_dic_key(dic, 'impositiontype')))
        else:
            self.imposition_type = None
        # Fields
        self.jurisdiction_level = get_dic_item(dic, get_attr_key(dic, 'jurisdictionlevel'))

    def __str__(self):
        print_str = "jurisdiction_level = %s, imposition_type = %s" \
                    % (self.jurisdiction_level, self.imposition_type)
        return print_str


# UNIT TEST -----------------------------------------------------------------
def test_imposition():
    imposition_dictionary = {'jurisdiction_level': 'PARISH',
                             'imposition_type': {'userdefined': True, 'impositiontypeid': 6,
                                                 'withholdingtype': 'Withholding Type'}}
    imposition = Imposition(imposition_dictionary)
    try:
        assert imposition.jurisdiction_level == 'PARISH', \
            'jurisdiction_level assertion failed. ' 'Expected PARISH'
        assert imposition.imposition_type.user_defined is True, \
            'imposition_type.user_defined assertion failed. ' 'Expected True'

    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_imposition()
    finally:
        print("Test of Imposition PASSED")
