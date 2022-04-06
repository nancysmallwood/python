# taxResult	optional	TaxResultCode
# taxType	optional	Taxing
# maxTaxIndicator	optional	Boolean
# situs	optional	TaxingLocationCode
# notRegisteredIndicator	optional	Boolean
# inputOutputType	optional	InputOutputCode
# taxCode	optional	String
# vertexTaxCode	optional	String
# reasonCode	optional	String (1 - 4)
# filingCategoryCode	optional	Positive Integer (1 - 99999)
# isService	optional	Boolean
# rateClassification	optional	String
# taxCollectedFromParty	optional	TaxCollectedFromParty
# taxStructure	optional	TaxStructureCode
from calcobjects.jurisdiction import Jurisdiction
from util.dictionary_util import get_dic_item, get_attr_key, get_dic_key


class Tax:
    # The init method or constructor
    def __init__(self, dic):
        self.taxresult = None
        self.taxtype = None
        self.taxresult = None
        self.maxtaxindicator = None
        self.notregisteredindicator = None
        self.inputoutputtype = None
        self.taxcode = None
        self.vertextaxcode = None
        self.reasoncode = None
        self.filingcategorycode = None
        self.isservice = None
        self.rateclassification = None
        self.taxcollectedfromparty = None
        self.taxstructure = None
        self.jurisdiction = Jurisdiction(dic)
        if dic is not None:
            self.taxresult = get_dic_item(dic, get_attr_key(dic, 'taxresult'))
            self.taxtype = get_dic_item(dic, get_attr_key(dic, 'taxtype'))
            self.taxresult = get_dic_item(dic, get_attr_key(dic, 'taxresult'))
            self.maxtaxindicator = get_dic_item(dic, get_attr_key(dic, 'maxtaxindicator'))
            self.notregisteredindicator = get_dic_item(dic, get_attr_key(dic, 'notregisteredindicator'))
            self.inputoutputtype = get_dic_item(dic, get_attr_key(dic, 'inputoutputtype'))
            self.taxcode = get_dic_item(dic, get_attr_key(dic, 'taxcode'))
            self.vertextaxcode = get_dic_item(dic, get_attr_key(dic, 'vertextaxcode'))
            self.reasoncode = get_dic_item(dic, get_attr_key(dic, 'reasoncode'))
            self.filingcategorycode = get_dic_item(dic, get_attr_key(dic, 'filingcategorycode'))
            self.isservice = get_dic_item(dic, get_attr_key(dic, 'isservice'))
            self.rateclassification = get_dic_item(dic, get_attr_key(dic, 'rateclassification'))
            self.taxcollectedfromparty = get_dic_item(dic, get_attr_key(dic, 'taxcollectedfromparty'))
            self.taxstructure = get_dic_item(dic, get_attr_key(dic, 'taxstructure'))
            if get_dic_key(dic, 'jurisdiction') is not None:
                self.jurisdiction = Jurisdiction(get_dic_item(dic, get_dic_key(dic, 'jurisdiction')))

