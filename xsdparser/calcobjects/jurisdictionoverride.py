# DeductionOverride	0 - 1
# ImpositionType	0 - 1
# jurisdictionLevel	required	JurisdictionLevelCode
# RateOverride	0 - 1	Decimal
from calcobjects.deductionoverride import DeductionOverride
from calcobjects.impositiontype import ImpositionType
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key


class JurisdictionOverride:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'deductionoverride') is not None:
            self.deduction_override = DeductionOverride(get_dic_item(dic, get_dic_key(dic, 'deductionoverride')))
        else:
            self.deduction_override = None
        if get_dic_key(dic, 'impositiontype') is not None:
            self.imposition_type = ImpositionType(get_dic_item(dic, get_dic_key(dic, 'impositiontype')))
        else:
            self.imposition_type = None
        # Fields
        self.jurisdiction_level = get_dic_item(dic, get_attr_key(dic, 'jurisdictionlevel'))
        self.rate_override = get_dic_item(dic, get_attr_key(dic, 'rateoverride'))

    def __str__(self):
        print_str = "deduction_override = %s, imposition_type = %s, jurisdiction_level = %s, rate_override = %s" \
                    % (self.deduction_override, self.imposition_type, self.jurisdiction_level, self.rate_override)
        return print_str
