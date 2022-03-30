import os
import site
from calcobjects.login import Login
from calcobjects.quotation import Quotation
from calcobjects.taxregistration import test_tax_registration
from calcobjects.util import xml_to_dict

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
def get_dict_item(dict, key_name):
    try:
        item = dict[key_name]
        return item
    except KeyError:
        print(f'Item {key_name} is invalid.')
    return None


# Get the name of the dictionary key item
def get_key(dict, key_pattern):
    try:
        # Get key name used for soap envelope
        if len(list(dict)) == 0:
            return None
        # elif len(list(dict)) == 1:
        #     return dict[0]
        else:
            for key in list(dict):
                if key_pattern in key.lower():
                    return key
            return None
    except KeyError:
        print(f'Invalid SOAP request/response.')
        return None


# Test the payload to make sure it adheres to a common structure
def get_payload(dict):
    envelope_key = get_key(dict, 'envelope')
    if get_dict_item(dict, envelope_key) is not None:
        e = get_dict_item(dict, envelope_key)
        body_key = get_key(e, 'body')
        if get_dict_item(e, body_key) is not None:
            b = get_dict_item(e, body_key)
            v_envelope_key = get_key(b, 'vertexenvelope')
            if get_dict_item(b, v_envelope_key) is not None:
                v = get_dict_item(b, v_envelope_key)
                return v
    print('Invalid SOAP envelope')
    return None
    #     quotation = payload_dictionary['QuotationRequest']


def get_quotation(dict):
    quote = Quotation(dict)
    return quote


def get_login(dict):
    login = Login(dict)
    return login


def process_invoice(dict):
    print("Invoice")


def process_tax_area_lookup(dict):
    print("Tax Area Lookup")


def get_request_type(dict):
    if get_dict_item(dict, get_key(dict, 'login')) is not None:
        login = get_login(get_dict_item(dict, get_key(dict, 'login')))
        print(login)
    if get_dict_item(dict, get_key(dict, 'quotationrequest')) is not None:
        quote = get_quotation(get_dict_item(dict, get_key(dict, 'quotationrequest')))
        # test_tax_registration()
        print(quote)
    elif get_dict_item(dict, get_key(dict, 'invoicerequest')) is not None:
        process_invoice(dict)
    elif get_dict_item(dict, get_key(dict, 'taxarearequest')) is not None:
        process_tax_area_lookup(dict)
    else:
        return None
    return 0


# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    # site.addsitedir('.')
    new_path = os.path.join(os.path.dirname(__file__), 'calcobjects')
    print(new_path)
    site.addsitedir(new_path)

    dictionary = xml_to_dict(test_soap)
    if get_payload(dictionary) is not None:
        payload_dictionary = get_payload(dictionary)
        get_request_type(payload_dictionary)
        print('ok')
