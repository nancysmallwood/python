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
from calcobjects.exempt import Exempt
from calcobjects.impositiontype import ImpositionType
from calcobjects.jurisdiction import Jurisdiction
# from calcobjects.nontaxable import NonTaxable
# from calcobjects.taxable import Taxable
from calcobjects.taximposition import TaxImposition
from calcobjects.taxrule import TaxRule
from util.dictionary_util import get_dic_item, get_attr_key, get_dic_key, get_dic_bool_item


class Tax:
    # The init method or constructor
    def __init__(self, dic):
        self.taxresult = None
        self.taxtype = None
        self.situs = None
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
        self.calculated_tax = None
        self.effective_rate = None
        self.tax_apportionment_rate = None
        self.basis_reduction_percentage = None
        self.exempt = Exempt(None,None)
        self.nontaxable = Exempt(None,None)
        self.taxable = Exempt(None,None)
        self.reporting_basis = None
        self.imposition = TaxImposition(None)
        self.imposition_type = ImpositionType(None)
        self.tax_rule_id = TaxRule(None,None)
        self.basis_rule_id = TaxRule(None,None)
        self.inclusion_rule_id = TaxRule(None,None)
        self.max_tax_rule_id = TaxRule(None,None)
        self.recoverable_rule_id = TaxRule(None,None)
        self.post_calculation_evaluation_rule_id = TaxRule(None,None)
        self.credit_rule_id = TaxRule(None,None)
        self.basis_apportionment_rule_id = TaxRule(None,None)
        self.tax_rate_adjustment_rule_id = TaxRule(None,None)
        self.tax_apportionment_rule_id = TaxRule(None,None)
        self.accumulation_rule_id = TaxRule(None,None)
        self.telecom_unit_conversion_rule_id = TaxRule(None,None)
        self.reporting_basis_rule_id = TaxRule(None,None)
        self.recoverable_amount = None
        self.recoverable_percent = None
        self.blocking_recoverable_percent = None
        self.partial_exempt_recoverable_percent = None
        self.unrecoverable_amount = None
        self.original_tax = None
        self.included_tax = None
        self.nominal_rate = None
        self.markup_rate = None
        if dic is not None:
            self.taxresult = get_dic_item(dic, get_attr_key(dic, 'taxresult'))
            self.taxtype = get_dic_item(dic, get_attr_key(dic, 'taxtype'))
            self.situs = get_dic_item(dic, get_attr_key(dic, 'situs'))
            self.maxtaxindicator = get_dic_bool_item(dic, get_attr_key(dic, 'maxtaxindicator'))
            self.notregisteredindicator = get_dic_bool_item(dic, get_attr_key(dic, 'notregisteredindicator'))
            self.inputoutputtype = get_dic_item(dic, get_attr_key(dic, 'inputoutputtype'))
            self.taxcode = get_dic_item(dic, get_attr_key(dic, 'taxcode'))
            self.vertextaxcode = get_dic_item(dic, get_attr_key(dic, 'vertextaxcode'))
            self.reasoncode = get_dic_item(dic, get_attr_key(dic, 'reasoncode'))
            self.filingcategorycode = get_dic_item(dic, get_attr_key(dic, 'filingcategorycode'))
            self.isservice = get_dic_bool_item(dic, get_attr_key(dic, 'isservice'))
            self.rateclassification = get_dic_item(dic, get_attr_key(dic, 'rateclassification'))
            self.taxcollectedfromparty = get_dic_item(dic, get_attr_key(dic, 'taxcollectedfromparty'))
            self.taxstructure = get_dic_item(dic, get_attr_key(dic, 'taxstructure'))
            if get_dic_key(dic, 'jurisdiction') is not None:
                self.jurisdiction = Jurisdiction(get_dic_item(dic, get_dic_key(dic, 'jurisdiction')))
            self.calculated_tax = get_dic_item(dic, get_attr_key(dic, 'calculatedtax'))
            self.effective_rate = get_dic_item(dic, get_attr_key(dic, 'effectiverate'))
            self.tax_apportionment_rate = get_dic_item(dic, get_attr_key(dic, 'taxapportionmentrate'))
            self.basis_reduction_percentage = get_dic_item(dic, get_attr_key(dic, 'basisreductionpercentage'))
            self.exempt = Exempt(get_dic_item(dic, get_dic_key(dic, 'exempt')),'exempt')
            self.nontaxable = Exempt(get_dic_item(dic, get_dic_key(dic, 'nontaxable')),'nontaxable')
            self.taxable = Exempt(get_dic_item(dic, get_dic_key(dic, 'taxable')),'taxable')
            self.reporting_basis = get_dic_item(dic, get_attr_key(dic, 'reportingbasis'))
            self.imposition = TaxImposition(get_dic_item(dic, get_dic_key(dic, 'imposition')))
            self.imposition_type = ImpositionType(get_dic_item(dic, get_dic_key(dic, 'impositiontype')))
            self.tax_rule_id = TaxRule(get_dic_item(dic, get_dic_key(dic, 'taxruleid')),'taxruleid')
            self.basis_rule_id = TaxRule(get_dic_item(dic, get_dic_key(dic, 'basisruleid')),'basisruleid')
            self.inclusion_rule_id = TaxRule(get_dic_item(dic, get_dic_key(dic, 'inclusionruleid')),'inclusionruleid')
            self.max_tax_rule_id = TaxRule(get_dic_item(dic, get_dic_key(dic, 'maxtaxruleid')),'maxtaxruleid')
            self.recoverable_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'recoverableruleid')),'recoverableruleid')
            self.post_calculation_evaluation_rule_id = \
                TaxRule(get_dic_item
                        (dic, get_dic_key(dic, 'postcalculationevaluationruleid')),'postcalculationevaluationruleid')
            self.credit_rule_id = TaxRule(get_dic_item(dic, get_dic_key(dic, 'creditruleid')), 'creditruleid')
            self.basis_apportionment_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'basisapportionmentruleid')), 'basisapportionmentruleid')
            self.tax_rate_adjustment_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'taxrateadjustmentruleid')), 'taxrateadjustmentruleid')
            self.tax_apportionment_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'taxapportionmentruleid')), 'taxapportionmentruleid')
            self.accumulation_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'accumulationruleid')), 'accumulationruleid')
            self.telecom_unit_conversion_rule_id = \
                TaxRule(get_dic_item(dic,
                                     get_dic_key(dic, 'telecomunitconversionruleid')),'telecomunitconversionruleid')
            self.reporting_basis_rule_id = \
                TaxRule(get_dic_item(dic, get_dic_key(dic, 'reportingbasisruleid')), 'reportingbasisruleid')
            self.recoverable_amount = get_dic_item(dic, get_attr_key(dic, 'recoverableamount'))
            self.recoverable_percent = get_dic_item(dic, get_attr_key(dic, 'recoverablepercent'))
            self.blocking_recoverable_percent = get_dic_item(dic, get_attr_key(dic, 'blockingrecoverablepercent'))
            self.partial_exempt_recoverable_percent = \
                get_dic_item(dic, get_attr_key(dic, 'partialexemptrecoverablepercent'))
            self.unrecoverable_amount = get_dic_item(dic, get_attr_key(dic, 'unrecoverableamount'))
            self.original_tax = get_dic_item(dic, get_attr_key(dic, 'originaltax'))
            self.included_tax = get_dic_item(dic, get_attr_key(dic, 'includedtax'))
            self.nominal_rate = get_dic_item(dic, get_attr_key(dic, 'nominalrate'))
            self.markup_rate = get_dic_item(dic, get_attr_key(dic, 'markuprate'))