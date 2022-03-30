# lineItemNumber	optional	Long
# lineItemId	optional	String (1 - 40)
# Seller	0 - 1
# Customer	0 - 1
# Product	0 - 1
# Quantity	0 - 1
# taxDate	optional	Date (yyyy-mm-dd)
# isMulticomponent	optional	Boolean
# locationCode	optional	String (1 - 20)
# deliveryTerm	optional	DeliveryTermCode
# postingDate	optional	Date (yyyy-mm-dd)
# costCenter	optional	String (1 - 40)
# departmentCode	optional	String (1 - 40)
# generalLedgerAccount	optional	String (1 - 40)
# materialCode	optional	String (1 - 40)
# projectNumber	optional	String (1 - 40)
# usage	optional	String (1 - 40)
# usageClass	optional	String (1 - 40)
# vendorSKU	optional	String (1 - 40)
# countryOfOriginISOCode	optional	String (0 - 3)
# modeOfTransport	optional	Positive Integer (1 - 99)
# natureOfTransaction	optional	Positive Integer (1 - 999)
# intrastatCommodityCode	optional	String (1 - 8)
# netMassKilograms	optional	Integer
# taxIncludedIndicator	optional	Boolean
# transactionType	optional	SaleTransaction
# simplificationCode	optional	SimplificationCode
# titleTransfer	optional	PointOfTitleTransferCode
# chainTransactionPhase	optional	ChainTransactionPhaseCode
# exportProcedure	optional	String (1 - 20)
# materialOrigin	optional	String (1 - 60)
# Freight	0 - 1	Decimal
# FairMarketValue	0 - 1	Decimal
# Cost	0 - 1	Decimal
# UnitPrice	0 - 1	Decimal
# LandedCost	0 - 1	Decimal
# AmountBilledToDate	0 - 1	Decimal
# CompanyCodeCurrencyTaxableAmount	0 - 1	Decimal
# CompanyCodeCurrencyTaxAmount	0 - 1	Decimal
from calcobjects.commoditycode import CommodityCode
from calcobjects.customer import Customer
from calcobjects.flexiblefields import FlexibleFields
from calcobjects.linetype import LineType
from calcobjects.product import Product
from calcobjects.quantity import Quantity
from calcobjects.returnsfields import ReturnsFields
from calcobjects.seller import Seller
from calcobjects.supplementaryunit import SupplementaryUnit
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key
from calcobjects.volume import Volume
from calcobjects.weight import Weight


class LineItem:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'seller') is not None:
            self.seller = Seller(get_dic_item(dic, get_dic_key(dic, 'seller')))
        else:
            self.seller = None
        if get_dic_key(dic, 'customer') is not None:
            self.customer = Customer(get_dic_item(dic, get_dic_key(dic, 'customer')))
        else:
            self.customer = None
        if get_dic_key(dic, 'product') is not None:
            self.product = Product(get_dic_item(dic, get_dic_key(dic, 'product')))
        else:
            self.product = None
        if get_dic_key(dic, 'quantity') is not None:
            self.quantity = Quantity(get_dic_item(dic, get_dic_key(dic, 'quantity')))
        else:
            self.quantity = None
        if get_dic_key(dic, 'linetype') is not None:
            self.line_type = LineType(get_dic_item(dic, get_dic_key(dic, 'linetype')))
        else:
            self.line_type = None
        if get_dic_key(dic, 'commoditycode') is not None:
            self.commodity_code = CommodityCode(get_dic_item(dic, get_dic_key(dic, 'commoditycode')))
        else:
            self.commodity_code = None
        if get_dic_key(dic, 'weight') is not None:
            self.weight = Weight(get_dic_item(dic, get_dic_key(dic, 'weight')))
        else:
            self.weight = None
        if get_dic_key(dic, 'volume') is not None:
            self.volume = Volume(get_dic_item(dic, get_dic_key(dic, 'volume')))
        else:
            self.volume = None
        if get_dic_key(dic, 'supplementaryunit') is not None:
            self.supplementary_unit = SupplementaryUnit(get_dic_item(dic, get_dic_key(dic, 'supplementaryunit')))
        else:
            self.supplementary_unit = None
        if get_dic_key(dic, 'flexiblefields') is not None:
            self.flexible_fields = FlexibleFields(get_dic_item(dic, get_dic_key(dic, 'flexiblefields')))
        else:
            self.flexible_fields = None
        if get_dic_key(dic, 'returnsfields') is not None:
            self.returns_fields = ReturnsFields(get_dic_item(dic, get_dic_key(dic, 'returnsfields')))
        else:
            self.returns_fields = None
        # Fields
        self.line_item_number = get_dic_item(dic, get_attr_key(dic, 'lineitemnumber'))
        self.line_item_id = get_dic_item(dic, get_attr_key(dic, 'lineitemid'))
        self.tax_date = get_dic_item(dic, get_attr_key(dic, 'taxdate'))
        self.is_multicomponent = get_dic_item(dic, get_attr_key(dic, 'ismulticomponent'))
        self.location_code = get_dic_item(dic, get_attr_key(dic, 'locationcode'))

        self.delivery_term = get_dic_item(dic, get_attr_key(dic, 'deliveryterm'))
        self.posting_date = get_dic_item(dic, get_attr_key(dic, 'postingdate'))
        self.cost_center = get_dic_item(dic, get_attr_key(dic, 'costcenter'))
        self.department_code = get_dic_item(dic, get_attr_key(dic, 'departmentcode'))
        self.general_ledger_account = get_dic_item(dic, get_attr_key(dic, 'generalledgeraccount'))

        self.material_code = get_dic_item(dic, get_attr_key(dic, 'materialcode'))
        self.project_number = get_dic_item(dic, get_attr_key(dic, 'projectnumber'))
        self.usage = get_dic_item(dic, get_attr_key(dic, 'usage'))
        self.usage_class = get_dic_item(dic, get_attr_key(dic, 'usageclass'))
        self.vendor_sku = get_dic_item(dic, get_attr_key(dic, 'vendorsku'))

        self.country_of_origin_iso_code = get_dic_item(dic, get_attr_key(dic, 'countryoforiginisocode'))
        self.mode_of_transport = get_dic_item(dic, get_attr_key(dic, 'modeoftransport'))
        self.nature_of_transaction = get_dic_item(dic, get_attr_key(dic, 'natureoftransaction'))
        self.intrastat_commodity_code = get_dic_item(dic, get_attr_key(dic, 'intrastatcommoditycode'))
        self.net_mass_kilograms = get_dic_item(dic, get_attr_key(dic, 'netmasskilograms'))

        self.tax_included_indicator = get_dic_item(dic, get_attr_key(dic, 'taxincludedindicator'))
        self.transaction_type = get_dic_item(dic, get_attr_key(dic, 'transactiontype'))
        self.simplification_code = get_dic_item(dic, get_attr_key(dic, 'simplificationcode'))
        self.title_transfer = get_dic_item(dic, get_attr_key(dic, 'titletransfer'))
        self.chain_transaction_phase = get_dic_item(dic, get_attr_key(dic, 'chaintransactionphase'))

        self.export_procedure = get_dic_item(dic, get_attr_key(dic, 'exportprocedure'))
        self.material_origin = get_dic_item(dic, get_attr_key(dic, 'materialorigin'))
        self.freight = get_dic_item(dic, get_attr_key(dic, 'freight'))
        self.fair_market_value = get_dic_item(dic, get_attr_key(dic, 'fairmarketvalue'))
        self.cost = get_dic_item(dic, get_attr_key(dic, 'cost'))

        self.unit_price = get_dic_item(dic, get_attr_key(dic, 'unitprice'))
        self.landed_cost = get_dic_item(dic, get_attr_key(dic, 'landedcost'))
        self.amount_billed_to_date = get_dic_item(dic, get_attr_key(dic, 'amountbilledtodate'))
        self.company_code_currency_taxable_amount = get_dic_item(dic, get_attr_key(dic, 'companycodecurrencytaxableamount'))
        self.company_code_currency_tax_amount = get_dic_item(dic, get_attr_key(dic, 'companycodecurrencytaxamount'))

    def __str__(self):
        print_str = "\nline_item_number = %s, \nline_item_id = %s, \ntax_date = %s, \nis_multicomponent = %s," \
                    "\nlocation_code = %s, \ndelivery_term = %s, \nposting_date = %s, \ncost_center = %s, " \
                    "\ndepartment_code = %s, \ngeneral_ledger_account = %s, \nmaterial_code = %s, " \
                    "\nproject_number = %s, " \
                    "\nusage = %s, \nusage_class = %s, \nvendor_sku = %s, \ncountry_of_origin_iso_code = %s, " \
                    "\nmode_of_transport = %s, \nnature_of_transaction = %s, \nintrastat_commodity_code = %s, " \
                    "\nnet_mass_kilograms = %s, \ntax_included_indicator = %s, \ntransaction_type = %s, " \
                    "\nsimplification_code = %s, \ntitle_transfer = % s, \nchain_transaction_phase = % s, " \
                    "\nexport_procedure = % s, \nmaterial_origin = % s, \nfreight = % s, \nfair_market_value = % s, " \
                    "\ncost = % s, \nunit_price = % s, \nlanded_cost = % s, \namount_billed_to_date = % s, "\
                    "\ncompany_code_currency_taxable_amount = % s, \ncompany_code_currency_tax_amount = % s, " \
                    "\nseller = %s,"\
                    "\ncustomer = %s, \nproduct = %s, \nquantity = %s, " \
                    "\nline_type = %s, \ncommodity_code = %s, \nweight = %s, \nvolume = %s, " \
                    "\nsupplementaryunit = %s, \nflexible_fields = %s, \nreturns_fields = %s" \
                    % (self.line_item_number, self.line_item_id,self.tax_date, self.is_multicomponent,
                       self.location_code, self.delivery_term, self.posting_date, self.cost_center,
                       self.department_code, self.general_ledger_account, self.material_code,
                       self.project_number,
                       self.usage, self.usage_class, self.vendor_sku, self.country_of_origin_iso_code,
                       self.mode_of_transport, self.nature_of_transaction, self.intrastat_commodity_code,
                       self.net_mass_kilograms, self.tax_included_indicator, self.transaction_type,
                       self.simplification_code, self.title_transfer, self.chain_transaction_phase,
                       self.export_procedure, self.material_origin, self.freight, self.fair_market_value,
                       self.cost, self.unit_price, self.landed_cost, self.amount_billed_to_date,
                       self.company_code_currency_taxable_amount,self.company_code_currency_tax_amount,
                       self.seller,
                       self.customer, self.product, self.quantity,
                       self.line_type, self.commodity_code,self.weight,self.volume,
                       self.supplementary_unit, self.flexible_fields, self.returns_fields)
        return print_str


