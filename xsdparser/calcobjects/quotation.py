import json

from calcobjects.currency import Currency


# Parameter - expects a dictionary for Quotation init
from calcobjects.util import get_attr_key, get_dic_key, get_dic_item


class Quotation:
    # The init method or constructor
    def __init__(self, dic):
        self.company_code_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'companycodecurrency')))
        self.original_currency = Currency(get_dic_item(dic, get_dic_key(dic, 'originalcurrency')))
        self.currency = Currency(get_dic_item(dic, get_dic_key(dic, 'currency')))
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
                    "\nPayment Date = %s, \nDocument Sequence Id = %s, \nTax Point Date = %s" \
                    % (self.currency, self.original_currency, self.company_code_currency,
                       self.accumulation_document_number, self.accumulation_customer_number,
                       self.document_type,self.billing_type,self.order_type,
                       self.posting_date,self.location_code,self.return_assisted_parameters_indicator,
                       self.return_generated_line_items_indicator,self.delivery_term,
                       self.document_date,self.transaction_id,self.transaction_type,
                       self.simplification_code,self.round_at_line_level,self.payment_date,
                       self.document_sequence_id,self.tax_point_date)
        return print_str
