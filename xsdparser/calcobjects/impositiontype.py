# userDefined	optional	Boolean
# impositionTypeId	optional	Positive Integer
# withholdingType	optional	String
from calcobjects.util import get_attr_key, get_dic_item


class ImpositionType:
    # The init method or constructor
    def __init__(self, dic):
        self.imposition_type = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.user_defined = get_dic_item(dic, get_attr_key(dic, 'userdefined'))
        self.imposition_type_id = get_dic_item(dic, get_attr_key(dic, 'impositiontypeid'))
        self.withholding_type = get_dic_item(dic, get_attr_key(dic, 'withholdingtype'))

    def __str__(self):
        print_str = "user_defined = %s, imposition_type_id = %s, withholding_type = %s" \
                    % (self.user_defined, self.imposition_type_id, self.withholding_type)
        return print_str


# UNIT TEST -----------------------------------------------------------------
def test_imposition_type():
    imposition_type_dictionary = {'userdefined': True,
                                  'impositiontypeid': 6,
                                  'withholdingtype': 'Withholding Type'}
    imposition_type = ImpositionType(imposition_type_dictionary)
    try:
        assert imposition_type.user_defined == True, \
            'user_defined assertion failed. ' 'Expected True'
        assert imposition_type.imposition_type_id == 6, 'imposition_type_id assertion failed. ' 'Expected 6'
        assert imposition_type.withholding_type == 'Withholding Type', 'withholding_type assertion failed. ' \
                                                                       'Expected "Withholding Type"'
    except AssertionError as msg:
        print(msg)


# MAIN -----------------------------------------------------------------
# Executes unit test
if __name__ == '__main__':
    try:
        test_imposition_type()
    finally:
        print("Test of ImpositionType PASSED")
