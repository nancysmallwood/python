from calcobjects.currency import Currency


# Parameter - expects a dictionary for Quotation init
from calcobjects.currencyconversionfactors import CurrencyConversionFactors
from calcobjects.customer import Customer
from calcobjects.discount import Discount
from calcobjects.impositions import Impositions
from calcobjects.jurisdictionoverrides import JurisdictionOverrides
from calcobjects.lineitems import LineItems
from calcobjects.seller import Seller
from calcobjects.situsoverride import SitusOverride
from calcobjects.taxoverride import TaxOverride
from util.dictionary_util import get_attr_key, get_dic_key, get_dic_item


class Quotation:
    # The init method or constructor
    def __init__(self, dic):
        # Objects
        if get_dic_key(dic, 'companycodecurrency') is not None:
            self.company_code_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'companycodecurrency')))
        else:
            self.company_code_currency = None
        if get_dic_key(dic, 'originalcurrency') is not None:
            self.original_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'originalcurrency')))
        else:
            self.original_currency = None
        if get_dic_key(dic, 'currency') is not None:
            self.currency = Currency(get_dic_item(dic, get_dic_key(dic, 'currency')))
        else:
            self.currency = None
        if get_dic_key(dic, 'seller') is not None:
            self.seller = Seller(get_dic_item(dic, get_dic_key(dic, 'seller')))
        else:
            self.seller = None
        if get_dic_key(dic, 'customer') is not None:
            self.customer = Customer(get_dic_item(dic, get_dic_key(dic, 'customer')))
        else:
            self.customer = None
        if get_dic_key(dic, 'taxoverride') is not None:
            self.tax_override = TaxOverride(get_dic_item(dic, get_dic_key(dic, 'taxoverride')))
        else:
            self.tax_override = None
        if get_dic_key(dic, 'situsoverride') is not None:
            self.situs_override = SitusOverride(get_dic_item(dic, get_dic_key(dic, 'situsoverride')))
        else:
            self.tax_override = None
        if get_dic_key(dic, 'discount') is not None:
            self.discount = Discount(get_dic_item(dic, get_dic_key(dic, 'discount')))
        else:
            self.discount = None
        # Lists of Objects
        if get_dic_key(dic, 'impositiontoprocess') is not None:
            self.impositions = Impositions(get_dic_item(dic, get_dic_key(dic, 'impositiontoprocess')))
        else:
            self.impositions = None
        if get_dic_key(dic, 'lineitem') is not None:
            self.line_items = LineItems(get_dic_item(dic, get_dic_key(dic, 'lineitem')))
        else:
            self.line_items = None
        if get_dic_key(dic, 'jurisdictionoverride') is not None:
            self.jurisdiction_overrides = \
                JurisdictionOverrides(get_dic_item(dic, get_dic_key(dic, 'jurisdictionoverride')))
        else:
            self.jurisdiction_overrides = None
        if get_dic_key(dic, 'currencyconversionfactors') is not None:
            self.currency_conversion_factors = \
                CurrencyConversionFactors(get_dic_item(dic, get_dic_key(dic, 'currencyconversionfactors')))
        else:
            self.currency_conversion_factors = None
        # Fields
        self.accumulation_document_number = get_dic_item(dic, get_attr_key(dic, 'accumulationdocumentnumber'))
        self.accumulation_customer_number = get_dic_item(dic, get_attr_key(dic, 'accumulationcustomernumber'))
        self.document_type = get_dic_item(dic, get_attr_key(dic, 'documenttype'))
        self.billing_type = get_dic_item(dic, get_attr_key(dic, 'billingtype'))
        self.order_type = get_dic_item(dic, get_attr_key(dic, 'ordertype'))
        self.posting_date = get_dic_item(dic, get_attr_key(dic, 'postingdate'))
        self.location_code = get_dic_item(dic, get_attr_key(dic, 'locationcode'))
        self.return_assisted_parameters_indicator = get_dic_item(dic, get_attr_key(dic, 'returnassistedparametersindicator'))
        self.return_generated_line_items_indicator = get_dic_item(dic, get_attr_key(dic, 'returngeneratedlineitemsindicator'))
        self.delivery_term = get_dic_item(dic, get_attr_key(dic, 'deliveryterm'))
        self.document_date = get_dic_item(dic, get_attr_key(dic, 'documentdate'))
        self.transaction_id = get_dic_item(dic, get_attr_key(dic, 'transactionid'))
        self.transaction_type = get_dic_item(dic, get_attr_key(dic, 'transactiontype'))
        self.simplification_code = get_dic_item(dic, get_attr_key(dic, 'simplificationcode'))
        self.round_at_line_level = get_dic_item(dic, get_attr_key(dic, 'roundatlinelevel'))
        self.payment_date = get_dic_item(dic, get_attr_key(dic, 'paymentdate'))
        self.document_sequence_id = get_dic_item(dic, get_attr_key(dic, 'documentsequenceid'))
        self.tax_point_date = get_dic_item(dic, get_attr_key(dic, 'taxpointdate'))

    def __str__(self):
        print_str = "Currency = %s, \nOriginal Currency = %s, \nCompany Code Currency = %s" \
                    "\nAccumulation Document Number = %s, \nAccumulation Customer Number = %s" \
                    "\nDocument Type = %s, \nBilling Type = %s, \nOrder Type = %s, \nPosting Date = %s, "\
                    "\nLocation Code = %s, \nReturn Assisted Parameters Indicator = %s, " \
                    "\nReturn Generated Line Items Indicator = %s, \nDelivery Term = %s, " \
                    "\nDocument Date = %s, \nTransaction Id = %s, \nTransaction_type = %s, " \
                    "\nSimplification Code = %s, \nRound At Line Level = %s, " \
                    "\nPayment Date = %s, \nDocument Sequence Id = %s, \nTax Point Date = %s, \nSeller = %s, " \
                    "\nCustomer = %s, \nTax Override = %s, \nDiscount = %s," \
                    "\nCurrency Conversion Factors = %s, \nJurisdiction Overrides = %s, " \
                    "\nImpositions to Process = %s, " \
                    "\nLine Items = %s" \
                    % (self.currency, self.original_currency, self.company_code_currency,
                       self.accumulation_document_number, self.accumulation_customer_number,
                       self.document_type,self.billing_type,self.order_type,
                       self.posting_date,self.location_code,self.return_assisted_parameters_indicator,
                       self.return_generated_line_items_indicator,self.delivery_term,
                       self.document_date,self.transaction_id,self.transaction_type,
                       self.simplification_code,self.round_at_line_level,self.payment_date,
                       self.document_sequence_id,self.tax_point_date,self.seller,self.customer,
                       self.tax_override,self.discount,
                       self.currency_conversion_factors,self.jurisdiction_overrides,
                       self.impositions,self.line_items)
        return print_str
