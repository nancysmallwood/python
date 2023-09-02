import json

from calcobjects.applicationdata import ApplicationData
from calcobjects.login import Login
from calcobjects.payload import Payload
from calcobjects.ospmessage import OSPMessage
from util.dictionary_util import clean_nones

test_soap = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><VertexEnvelope ' \
            'xmlns="urn:vertexinc:o-series:tps:7:0"><Login><TrustedId>7649555430638576</TrustedId></Login>' \
            '<QuotationRequest documentNumber="Micls" returnAssistedParametersIndicator="true" ' \
            'documentDate="2021-02-09-06:00" transactionType="SALE"><Currency isoCurrencyCodeAlpha="CAD"/>' \
            '<Seller><Company>4000</Company></Seller><LineItem lineItemNumber="1" ' \
            'lineItemId="19f5ea7f12e642eabab81e70ba"><Customer><Destination locationCode="3938"/>' \
            '</Customer><Product productClass="4020"/><Quantity unitOfMeasure="EA">2.0</Quantity>' \
            '<ExtendedPrice>14.43</ExtendedPrice></LineItem><LineItem lineItemNumber="2" ' \
            'lineItemId="105f34536d04a49a3e1432b3b8"><Customer><Destination locationCode="3938"/>' \
            '</Customer><Product productClass="199"/><Quantity unitOfMeasure="EA">1.0</Quantity><ExtendedPrice>0.0' \
            '</ExtendedPrice></LineItem></QuotationRequest></VertexEnvelope></soap:Body></soap:Envelope>'


# Get the Dictionary item by key name
# Returns 0 if key does not exist
def get_dict_item(dic, key_name):
    try:
        item = dic[key_name]
        return item
    except KeyError:
        print(f'Key Error.  get_dict_item()')
        return None
    return None


# Get the name of the dictionary key item
def get_key(dic, key_pattern):
    try:
        # Get key name used for soap envelope
        if len(list(dic)) == 0:
            return None
        else:
            for key in list(dic):
                if key_pattern in key.lower():
                    return key
            return None
    except KeyError:
        print(f'Invalid SOAP request/response.')
        return None


# String off the envelope elements and return the core XML
def get_payload(dic):
    envelope_key = get_key(dic, 'envelope')
    if get_dict_item(dic, envelope_key) is not None:
        e = get_dict_item(dic, envelope_key)
        body_key = get_key(e, 'body')
        if get_dict_item(e, body_key) is not None:
            b = get_dict_item(e, body_key)
            v_envelope_key = get_key(b, 'vertexenvelope')
            if get_dict_item(b, v_envelope_key) is not None:
                v = get_dict_item(b, v_envelope_key)
                return v
    print('Invalid SOAP envelope')
    return None


def get_login(dic):
    login = Login(get_login_dictionary(dic))
    return login


def get_application_data(dic):
    application_data = ApplicationData(get_application_data_dictionary(dic))
    return application_data


def get_json_payload(dic):
    if dic is None:
        return None
    else:
        payload = Payload(get_login(dic),
                          get_application_data(dic),
                          get_calc_message_type(dic),
                          get_calc_message(dic))
        # Serialization
        payload_json = json.dumps(payload, default=lambda o: o.__dict__, indent=4)
        return payload_json


def get_login_dictionary(dic):
    if get_dict_item(dic, get_key(dic, 'login')) is not None:
        return get_dict_item(dic, get_key(dic, 'login'))
    else:
        return None


def get_calc_message(dic):
    return OSPMessage(get_calc_message_dictionary(dic))


def get_calc_message_type(dic):
    if get_dict_item(dic, get_key(dic, 'quotationrequest')) is not None:
        return 'quotationrequest'
    elif get_dict_item(dic, get_key(dic, 'quotationresponse')) is not None:
        return 'quotationresponse'
    elif get_dict_item(dic, get_key(dic, 'invoicerequest')) is not None:
        return 'invoicerequest'
    elif get_dict_item(dic, get_key(dic, 'invoiceresponse')) is not None:
        return 'invoiceresponse'
    elif get_dict_item(dic, get_key(dic, 'accrualrequest')) is not None:
        return 'accrualrequest'
    elif get_dict_item(dic, get_key(dic, 'accrualresponse')) is not None:
        return 'accrualresponse'
    elif get_dict_item(dic, get_key(dic, 'taxarearequest')) is not None:
        return 'taxarearequest'
    elif get_dict_item(dic, get_key(dic, 'taxarearesponse')) is not None:
        return 'taxarearesponse'
    elif get_dict_item(dic, get_key(dic, 'transactionexistsrequest')) is not None:
        return 'transactionexistsrequest'
    elif get_dict_item(dic, get_key(dic, 'transactionexistsresponse')) is not None:
        return 'transactionexistsresponse'
    elif get_dict_item(dic, get_key(dic, 'arbillingsyncrequest')) is not None:
        return 'arbillingsyncrequest'
    elif get_dict_item(dic, get_key(dic, 'arbillingsyncresponse')) is not None:
        return 'arbillingsyncresponse'
    elif get_dict_item(dic, get_key(dic, 'purchaseorderrequest')) is not None:
        return 'purchaseorderrequest'
    elif get_dict_item(dic, get_key(dic, 'purchaseorderresponse')) is not None:
        return 'purchaseorderresponse'
    elif get_dict_item(dic, get_key(dic, 'reversalrequest')) is not None:
        return 'reversalrequest'
    elif get_dict_item(dic, get_key(dic, 'reversalresponse')) is not None:
        return 'reversalresponse'
    elif get_dict_item(dic, get_key(dic, 'distributetaxrequest')) is not None:
        return 'distributetaxrequest'
    elif get_dict_item(dic, get_key(dic, 'distributetaxresponse')) is not None:
        return 'distributetaxresponse'
    elif get_dict_item(dic, get_key(dic, 'invoiceverificationrequest')) is not None:
        return 'invoiceverificationrequest'
    elif get_dict_item(dic, get_key(dic, 'invoiceverificationresponse')) is not None:
        return 'invoiceverificationresponse'
    elif get_dict_item(dic, get_key(dic, 'rollbackrequest')) is not None:
        return 'rollbackrequest'
    elif get_dict_item(dic, get_key(dic, 'rollbackresponse')) is not None:
        return 'rollbackresponse'
    elif get_dict_item(dic, get_key(dic, 'distributetaxprocurementrequest')) is not None:
        return 'distributetaxprocurementrequest'
    elif get_dict_item(dic, get_key(dic, 'distributetaxprocurementresponse')) is not None:
        return 'distributetaxprocurementresponse'
    elif get_dict_item(dic, get_key(dic, 'deleterequest')) is not None:
        return 'deleterequest'
    elif get_dict_item(dic, get_key(dic, 'deleteresponse')) is not None:
        return 'deleteresponse'
    else:
        return ''


def get_calc_message_dictionary(dic):
    if get_dict_item(dic, get_key(dic, 'quotationrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'quotationrequest'))
    elif get_dict_item(dic, get_key(dic, 'quotationresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'quotationresponse'))

    elif get_dict_item(dic, get_key(dic, 'invoicerequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'invoicerequest'))
    elif get_dict_item(dic, get_key(dic, 'invoiceresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'invoiceresponse'))

    elif get_dict_item(dic, get_key(dic, 'accrualrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'accrualrequest'))
    elif get_dict_item(dic, get_key(dic, 'accrualresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'accrualresponse'))

    elif get_dict_item(dic, get_key(dic, 'taxarearequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'taxarearequest'))
    elif get_dict_item(dic, get_key(dic, 'taxarearesponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'taxarearesponse'))

    elif get_dict_item(dic, get_key(dic, 'transactionexistsrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'transactionexistsrequest'))
    elif get_dict_item(dic, get_key(dic, 'transactionexistsresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'transactionexistsresponse'))

    elif get_dict_item(dic, get_key(dic, 'arbillingsyncrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'arbillingsyncrequest'))
    elif get_dict_item(dic, get_key(dic, 'arbillingsyncresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'arbillingsyncresponse'))

    elif get_dict_item(dic, get_key(dic, 'purchaseorderrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'purchaseorderrequest'))
    elif get_dict_item(dic, get_key(dic, 'purchaseorderresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'purchaseorderresponse'))

    elif get_dict_item(dic, get_key(dic, 'reversalrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'reversalrequest'))
    elif get_dict_item(dic, get_key(dic, 'reversalresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'reversalresponse'))

    elif get_dict_item(dic, get_key(dic, 'distributetaxrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'distributetaxrequest'))
    elif get_dict_item(dic, get_key(dic, 'distributetaxresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'distributetaxresponse'))

    elif get_dict_item(dic, get_key(dic, 'invoiceverificationrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'invoiceverificationrequest'))
    elif get_dict_item(dic, get_key(dic, 'invoiceverificationresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'invoiceverificationresponse'))

    elif get_dict_item(dic, get_key(dic, 'rollbackrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'rollbackrequest'))
    elif get_dict_item(dic, get_key(dic, 'rollbackresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'rollbackresponse'))

    elif get_dict_item(dic, get_key(dic, 'distributetaxprocurementrequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'distributetaxprocurementrequest'))
    elif get_dict_item(dic, get_key(dic, 'distributetaxprocurementresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'distributetaxprocurementresponse'))

    elif get_dict_item(dic, get_key(dic, 'deleterequest')) is not None:
        return get_dict_item(dic, get_key(dic, 'deleterequest'))
    elif get_dict_item(dic, get_key(dic, 'deleteresponse')) is not None:
        return get_dict_item(dic, get_key(dic, 'deleteresponse'))
    else:
        return None


def get_application_data_dictionary(dic):
    if get_dict_item(dic, get_key(dic, 'applicationdata')) is not None:
        return get_dict_item(dic, get_key(dic, 'applicationdata'))
    else:
        return None

# def get_request_type(dic):
#     if get_dict_item(dic, get_key(dic, 'login')) is not None:
#         login = get_login(get_dict_item(dic, get_key(dic, 'login')))
#         # print(login)
#         return login
#     if get_dict_item(dic, get_key(dic, 'quotationrequest')) is not None:
#         quote = get_quotation(get_dict_item(dic, get_key(dic, 'quotationrequest')))
#         # print(quote)
#         return quote
#     if get_dict_item(dic, get_key(dic, 'applicationdata')) is not None:
#         application_data = get_application_data(get_dict_item(dic, get_key(dic, 'applicationdata')))
#         # print(application_data)
#         return application_data
#     elif get_dict_item(dic, get_key(dic, 'invoicerequest')) is not None:
#         process_invoice(dic)
#         return None
#     elif get_dict_item(dic, get_key(dic, 'taxarearequest')) is not None:
#         process_tax_area_lookup(dic)
#         return None
#     else:
#         return None


# def run(osp_location):
#     files = get_filenames(osp_location)
#     #for each_file in files:


# # MAIN -----------------------------------------------------------------
# if __name__ == '__main__':
#     new_path = os.path.join(os.path.dirname(__file__), 'calcobjects')
#     site.addsitedir(new_path)
#     new_path = os.path.join(os.path.dirname(__file__), 'util')
#     site.addsitedir(new_path)
#
#     dictionary = xml_to_dict(test_soap)
#     if get_payload(dictionary) is not None:
#         payload_dictionary = get_payload(dictionary)
#         login = get_login(payload_dictionary)
#         quote = get_quote(payload_dictionary)
#         application_data = get_application_data(payload_dictionary)
#         print('ok')
