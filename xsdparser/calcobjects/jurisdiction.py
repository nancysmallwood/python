# Jurisdiction	0 - 1
# jurisdictionLevel	required	JurisdictionLevelCode
# jurisdictionId	required	Integer (0 - 999999999)
# effectiveDate	optional	Date (yyyy-mm-dd)
# expirationDate	optional	Date (yyyy-mm-dd)
# externalJurisdictionCode	optional	String (0 - 20)
from util.dictionary_util import get_dic_item, get_attr_key


class Jurisdiction:
    # The init method or constructor
    def __init__(self, dic):
        self.jurisdictionlevel = None
        self.jurisdictionid = None
        self.effectivedate = None
        self.expirationdate = None
        self.externaljurisdictioncode = None
        if dic is not None:
            self.jurisdictionlevel = get_dic_item(dic, get_attr_key(dic, 'jurisdictionlevel'))
            self.jurisdictionid = get_dic_item(dic, get_attr_key(dic, 'jurisdictionid'))
            self.effectivedate = get_dic_item(dic, get_attr_key(dic, 'effectivedate'))
            self.expirationdate = get_dic_item(dic, get_attr_key(dic, 'expirationdate'))
            self.externaljurisdictioncode = get_dic_item(dic, get_attr_key(dic, 'externaljurisdictioncode'))

