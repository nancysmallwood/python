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
from calcobjects.discount import Discount
from calcobjects.flexiblefields import FlexibleFields
from calcobjects.impositions import Impositions
from calcobjects.jurisdictionoverrides import JurisdictionOverrides
from calcobjects.linetype import LineType
from calcobjects.product import Product
from calcobjects.quantity import Quantity
from calcobjects.returnsfields import ReturnsFields
from calcobjects.seller import Seller
from calcobjects.situsoverride import SitusOverride
from calcobjects.statisticalvalue import StatisticalValue
from calcobjects.supplementaryunit import SupplementaryUnit
from calcobjects.taxes import Taxes
from calcobjects.taxoverride import TaxOverride
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str, coalesce_bool, coalesce_num
from calcobjects.volume import Volume
from calcobjects.weight import Weight


class LineItem:
    # The init method or constructor
    def __init__(self, dic):
        self.taxes = Taxes(dic)
        self.seller = Seller(dic)
        self.customer = Customer(dic)
        self.product = Product(dic)
        self.quantity = Quantity(dic)
        self.line_type = LineType(dic)
        self.commodity_code = CommodityCode(dic)
        self.weight = Weight(dic)
        self.volume = Volume(dic)
        self.supplementary_unit = SupplementaryUnit(dic)
        self.flexible_fields = FlexibleFields(dic)
        self.returns_fields = ReturnsFields(dic)
        self.tax_override = TaxOverride(dic)
        self.imposition_to_process = Impositions(dic)
        self.jurisdiction_override = JurisdictionOverrides(dic)
        self.situs_override = SitusOverride(dic)
        self.statistical_value = StatisticalValue(dic)
        self.discount = Discount(dic)
        self.line_item_number = None
        self.line_item_id = None
        self.tax_date = None
        self.is_multicomponent = False
        self.location_code = None
        self.delivery_term = None
        self.posting_date = None
        self.cost_center = None
        self.department_code = None
        self.general_ledger_account = None
        self.material_code = None
        self.project_number = None
        self.usage = None
        self.usage_class = None
        self.vendor_sku = None
        self.country_of_origin_iso_code = None
        self.mode_of_transport = None
        self.nature_of_transaction = None
        self.intrastat_commodity_code = None
        self.net_mass_kilograms = None
        self.tax_included_indicator = False
        self.transaction_type = None
        self.simplification_code = None
        self.title_transfer = None
        self.chain_transaction_phase = None
        self.export_procedure = None
        self.material_origin = None
        self.freight = None
        self.fair_market_value = None
        self.cost = None
        self.unit_price = None
        self.landed_cost = None
        self.amount_billed_to_date = None
        self.company_code_currency_taxable_amount = None
        self.company_code_currency_tax_amount = None
        self.extended_price = None

        if dic is not None:
            # Objects
            if get_dic_key(dic, 'taxes') is not None:
                self.taxes = Taxes(get_dic_item(dic, get_dic_key(dic, 'taxes')))
            if get_dic_key(dic, 'seller') is not None:
                self.seller = Seller(get_dic_item(dic, get_dic_key(dic, 'seller')))
            if get_dic_key(dic, 'customer') is not None:
                self.customer = Customer(get_dic_item(dic, get_dic_key(dic, 'customer')))
            if get_dic_key(dic, 'product') is not None:
                self.product = Product(get_dic_item(dic, get_dic_key(dic, 'product')))
            if get_dic_key(dic, 'quantity') is not None:
                self.quantity = Quantity(get_dic_item(dic, get_dic_key(dic, 'quantity')))
            if get_dic_key(dic, 'linetype') is not None:
                self.line_type = LineType(get_dic_item(dic, get_dic_key(dic, 'linetype')))
            if get_dic_key(dic, 'commoditycode') is not None:
                self.commodity_code = CommodityCode(get_dic_item(dic, get_dic_key(dic, 'commoditycode')))
            if get_dic_key(dic, 'weight') is not None:
                self.weight = Weight(get_dic_item(dic, get_dic_key(dic, 'weight')))
            if get_dic_key(dic, 'volume') is not None:
                self.volume = Volume(get_dic_item(dic, get_dic_key(dic, 'volume')))
            if get_dic_key(dic, 'supplementaryunit') is not None:
                self.supplementary_unit = SupplementaryUnit(get_dic_item(dic, get_dic_key(dic, 'supplementaryunit')))
            if get_dic_key(dic, 'flexiblefields') is not None:
                self.flexible_fields = FlexibleFields(get_dic_item(dic, get_dic_key(dic, 'flexiblefields')))
            if get_dic_key(dic, 'returnsfields') is not None:
                self.returns_fields = ReturnsFields(get_dic_item(dic, get_dic_key(dic, 'returnsfields')))
            if get_dic_key(dic, 'taxoverride') is not None:
                self.tax_override = TaxOverride(get_dic_item(dic, get_dic_key(dic, 'taxoverride')))
            if get_dic_key(dic, 'impositiontoprocess') is not None:
                self.imposition_to_process = Impositions(get_dic_item(dic, get_dic_key(dic, 'impositiontoprocess')))
            if get_dic_key(dic, 'jurisdictionoverride') is not None:
                self.jurisdiction_override = JurisdictionOverrides(get_dic_item(dic, get_dic_key(dic, 'jurisdictionoverride')))
            if get_dic_key(dic, 'situsoverride') is not None:
                self.situs_override = SitusOverride(get_dic_item(dic, get_dic_key(dic, 'situsoverride')))
            if get_dic_key(dic, 'statisticalvalue') is not None:
                self.statistical_value = StatisticalValue(get_dic_item(dic, get_dic_key(dic, 'statisticalvalue')))
            if get_dic_key(dic, 'discount') is not None:
                self.discount = Discount(get_dic_item(dic, get_dic_key(dic, 'discount')))

            # Fields
            self.line_item_number = get_dic_item(dic, get_attr_key(dic, 'lineitemnumber'))
            self.line_item_id = get_dic_item(dic, get_attr_key(dic, 'lineitemid'))
            self.tax_date = get_dic_item(dic, get_attr_key(dic, 'taxdate'))
            if get_dic_item(dic, get_attr_key(dic, 'ismulticomponent')) is not None:
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

            if get_dic_item(dic, get_attr_key(dic, 'taxincludedindicator')) is not None:
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
            self.company_code_currency_taxable_amount = \
                get_dic_item(dic, get_attr_key(dic, 'companycodecurrencytaxableamount'))
            self.company_code_currency_tax_amount = \
                get_dic_item(dic, get_attr_key(dic, 'companycodecurrencytaxamount'))
            self.extended_price = get_dic_item(dic, get_attr_key(dic, 'extendedprice'))

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

    def to_json(self):
        return '{"lineItemNumber": %s, ' \
               '"taxDate": %s, ' \
               '"isMulticomponent": %s, ' \
               '"locationCode": %s, ' \
               '"deliveryTerm": %s, ' \
               '"postingDate": %s, ' \
               '"costCenter": %s, ' \
               '"departmentCode": %s, ' \
               '"generalLedgerAccount": %s, ' \
               '"materialCode": %s, ' \
               '"projectNumber": %s, ' \
               '"usage": %s, "usageClass": %s, "vendorSKU": %s, "countryOfOriginISOCode": %s,' \
               '"modeOfTransport": %s, "natureOfTransaction": %s, "intrastatCommodityCode": %s, "netMassKilograms": %s, "lineItemId": %s, ' \
               '"taxIncludedIndicator": %s, "transactionType": %s, "simplificationCode": %s, "titleTransfer": %s, "chainTransactionPhase": %s, ' \
               '"exportProcedure": %s, "materialOrigin": %s, ' \
               '"Seller": %s, "Customer": %s, "TaxOverride": %s, ' \
               '"ImpositionToProcess": %s, "JurisdictionOverride": %s, "SitusOverride": %s, "Product": %s, "LineType": %s, ' \
               '"CommodityCode": %s, "Quantity": %s, "Weight": %s, "Volume": %s, "SupplementaryUnit": %s, "StatisticalValue": %s, ' \
               '"Freight": %s, "FairMarketValue": %s, "Cost": %s, "UnitPrice": %s, "ExtendedPrice": %s, "LandedCost": %s, ' \
               '"Discount": %s, "AmountBilledToDate": %s, "CompanyCodeCurrencyTaxableAmount": %s, "CompanyCodeCurrencyTaxAmount": %s, "FlexibleFields": %s, "ReturnsFields": %s}' % \
               (coalesce_num(self.line_item_number),
                coalesce_str(self.tax_date),
                coalesce_bool(self.is_multicomponent),
                coalesce_str(self.location_code),
                coalesce_str(self.delivery_term),
                coalesce_str(self.posting_date),
                coalesce_str(self.cost_center),
                coalesce_str(self.department_code),
                coalesce_str(self.general_ledger_account),
                coalesce_bool(self.material_code),
                coalesce_str(self.project_number),
                coalesce_str(self.usage),
                coalesce_str(self.usage_class),
                coalesce_str(self.vendor_sku),
                coalesce_str(self.country_of_origin_iso_code),
                coalesce_num(self.mode_of_transport),
                coalesce_num(self.nature_of_transaction),
                coalesce_str(self.intrastat_commodity_code),
                coalesce_num(self.net_mass_kilograms),
                coalesce_str(self.line_item_id),
                coalesce_bool(self.tax_included_indicator),
                coalesce_str(self.transaction_type),
                coalesce_str(self.simplification_code),
                coalesce_str(self.title_transfer),
                coalesce_str(self.chain_transaction_phase),
                coalesce_str(self.export_procedure),
                coalesce_str(self.material_origin),
                self.seller.to_json(),
                self.customer.to_json(),
                self.tax_override.to_json(),
                self.imposition_to_process.to_json(),
                self.jurisdiction_override.to_json(),
                self.situs_override.to_json(),
                self.product.to_json(),
                self.line_type.to_json(),
                self.commodity_code.to_json(),
                self.quantity.to_json(),
                self.weight.to_json(),
                self.volume.to_json(),
                self.supplementary_unit.to_json(),
                self.statistical_value.to_json(),
                coalesce_num(self.freight),
                coalesce_num(self.fair_market_value),
                coalesce_num(self.cost),
                coalesce_num(self.unit_price),
                coalesce_num(self.extended_price),
                coalesce_num(self.landed_cost),
                self.discount.to_json(),
                coalesce_num(self.amount_billed_to_date),
                coalesce_num(self.company_code_currency_taxable_amount),
                coalesce_num(self.company_code_currency_tax_amount),
                self.flexible_fields.to_json(),
                self.returns_fields.to_json())
