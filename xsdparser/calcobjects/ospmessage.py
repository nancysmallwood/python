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
from util.dictionary_util import get_attr_key, get_dic_key, get_dic_item, coalesce_str, coalesce_bool, get_dic_bool_item


class OSPMessage:
    # The init method or constructor
    def __init__(self, dic):
        self.return_assisted_parameters_indicator = False
        self.return_generated_line_items_indicator = False
        self.round_at_line_level = False
        self.subtotal = get_dic_item(dic, get_attr_key(dic, 'subtotal'))
        self.total = get_dic_item(dic, get_attr_key(dic, 'total'))
        self.totaltax = get_dic_item(dic, get_attr_key(dic, 'totaltax'))

        # Objects
        self.company_code_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'companycodecurrency')))
        self.original_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'originalcurrency')))
        self.currency = Currency(get_dic_item(dic, get_dic_key(dic, 'currency')))
        self.seller = Seller(get_dic_item(dic, get_dic_key(dic, 'seller')))
        self.customer = Customer(get_dic_item(dic, get_dic_key(dic, 'customer')))
        self.tax_override = TaxOverride(get_dic_item(dic, get_dic_key(dic, 'taxoverride')))
        self.situs_override = SitusOverride(get_dic_item(dic, get_dic_key(dic, 'situsoverride')))
        self.discount = Discount(get_dic_item(dic, get_dic_key(dic, 'discount')))
        self.impositions = Impositions(get_dic_item(dic, get_dic_key(dic, 'impositiontoprocess')))
        self.line_items = LineItems(get_dic_item(dic, get_dic_key(dic, 'lineitem')))
        self.jurisdiction_overrides = \
            JurisdictionOverrides(get_dic_item(dic, get_dic_key(dic, 'jurisdictionoverride')))
        self.currency_conversion_factors = \
            CurrencyConversionFactors(get_dic_item(dic, get_dic_key(dic, 'currencyconversionfactors')))
        # Fields
        self.accumulation_document_number = get_dic_item(dic, get_attr_key(dic, 'accumulationdocumentnumber'))
        self.accumulation_customer_number = get_dic_item(dic, get_attr_key(dic, 'accumulationcustomernumber'))
        self.document_type = get_dic_item(dic, get_attr_key(dic, 'documenttype'))
        self.document_number = get_dic_item(dic, get_attr_key(dic, 'documentnumber'))
        self.billing_type = get_dic_item(dic, get_attr_key(dic, 'billingtype'))
        self.order_type = get_dic_item(dic, get_attr_key(dic, 'ordertype'))
        self.posting_date = get_dic_item(dic, get_attr_key(dic, 'postingdate'))
        self.location_code = get_dic_item(dic, get_attr_key(dic, 'locationcode'))
        if get_dic_bool_item(dic, get_attr_key(dic, 'returnassistedparametersindicator')) is not None:
            self.return_assisted_parameters_indicator = \
                get_dic_bool_item(dic, get_attr_key(dic, 'returnassistedparametersindicator'))
        if get_dic_bool_item(dic, get_attr_key(dic, 'returngeneratedlineitemsindicator')) is not None:
            self.return_generated_line_items_indicator = \
                get_dic_bool_item(dic, get_attr_key(dic, 'returngeneratedlineitemsindicator'))
        self.delivery_term = get_dic_item(dic, get_attr_key(dic, 'deliveryterm'))
        self.document_date = get_dic_item(dic, get_attr_key(dic, 'documentdate'))
        self.transaction_id = get_dic_item(dic, get_attr_key(dic, 'transactionid'))
        self.transaction_type = get_dic_item(dic, get_attr_key(dic, 'transactiontype'))
        self.simplification_code = get_dic_item(dic, get_attr_key(dic, 'simplificationcode'))
        if get_dic_bool_item(dic, get_attr_key(dic, 'roundatlinelevel')) is not None:
            self.round_at_line_level = get_dic_bool_item(dic, get_attr_key(dic, 'roundatlinelevel'))
        self.payment_date = get_dic_item(dic, get_attr_key(dic, 'paymentdate'))
        self.document_sequence_id = get_dic_item(dic, get_attr_key(dic, 'documentsequenceid'))
        self.tax_point_date = get_dic_item(dic, get_attr_key(dic, 'taxpointdate'))


    def __str__(self):
        print_str = "Currency = %s, \nOriginal Currency = %s, \nCompany Code Currency = %s" \
                    "\nDocument Number = %s, \nAccumulation Document Number = %s, \nAccumulation Customer Number = %s" \
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
                       self.document_number,self.accumulation_document_number, self.accumulation_customer_number,
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

    def to_json(self):
        return '{"documentNumber": %s, ' \
               '"accumulationDocumentNumber": %s, ' \
               '"accumulationCustomerNumber": %s, ' \
               '"documentType": %s, ' \
               '"billingType": %s, ' \
               '"orderType": %s, ' \
               '"postingDate": %s, ' \
               '"locationCode": %s, ' \
               '"returnAssistedParametersIndicator": %s, ' \
               '"returnGeneratedLineItemsIndicator": %s, ' \
               '"deliveryTerm": %s, ' \
               '"documentDate": %s, ' \
               '"transactionId": %s, ' \
               '"transactionType": %s, ' \
               '"simplificationCode": %s, ' \
               '"roundAtLineLevel": %s, ' \
               '"paymentDate": %s, ' \
               '"documentSequenceId": %s, ' \
               '"taxPointDate": %s, ' \
               '"Currency": %s, ' \
               '"OriginalCurrency": %s, ' \
               '"CompanyCodeCurrency": %s, ' \
               '"Seller": %s, ' \
               '"Customer": %s, ' \
               '"TaxOverride": %s, ' \
               '"ImpositionToProcess": %s, ' \
               '"JurisdictionOverride": %s, ' \
               '"SitusOverride": %s, ' \
               '"Discount": %s, ' \
               '"CurrencyConversionFactors": %s, ' \
               '"LineItems": %s}' % \
               (coalesce_str(self.document_number),
                coalesce_str(self.accumulation_document_number),
                coalesce_str(self.accumulation_customer_number),
                coalesce_str(self.document_type),
                coalesce_str(self.billing_type),
                coalesce_str(self.order_type),
                coalesce_str(self.posting_date),
                coalesce_str(self.location_code),
                coalesce_bool(self.return_assisted_parameters_indicator),
                coalesce_bool(self.return_generated_line_items_indicator),
                coalesce_str(self.delivery_term),
                coalesce_str(self.document_date),
                coalesce_str(self.transaction_id),
                coalesce_str(self.transaction_type),
                coalesce_str(self.simplification_code),
                coalesce_bool(self.round_at_line_level),
                coalesce_str(self.payment_date),
                coalesce_bool(self.document_sequence_id),
                coalesce_bool(self.tax_point_date),
                self.currency.to_json(),
                self.original_currency.to_json(),
                self.company_code_currency.to_json(),
                self.seller.to_json(),
                self.customer.to_json(),
                self.tax_override.to_json(),
                self.impositions.to_json(),
                self.jurisdiction_overrides.to_json(),
                self.situs_override.to_json(),
                self.discount.to_json(),
                self.currency_conversion_factors.to_json(),
                self.line_items.to_json())
