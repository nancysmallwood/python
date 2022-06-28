from pprint import pprint

import xmltodict

null = None


def xml_to_dict(payload):
    return xmltodict.parse(payload)


# Get the Dictionary item by key name
# Returns 0 if key does not exist
def get_dic_item(dic, key_name):
    try:
        if dic is None or key_name is None:
            return None
        else:
            item = dic[key_name]
            return item
    except KeyError:
        return null


# Get the Dictionary item by key name
# Returns 0 if key does not exist
def get_dic_bool_item(dic, key_name):
    try:
        if dic is None or key_name is None:
            return None
        else:
            item = dic[key_name]
            if isinstance(item, bool):
                return item
            elif isinstance(item, str):
                if item.lower() == 'false':
                    return False
                elif item.lower() == 'true':
                    return True
            else:
                return None
    except KeyError:
        return None

# Get the name of the dictionary attribute key
def get_attr_key(dic, key_pattern):
    try:
        if dic is None:
            return None
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


# Get the name of the dictionary key
def get_dic_key(dic, key_pattern):
    try:
        if dic is None:
            return None
        # Get key name used for soap envelope
        if len(list(dic)) == 0:
            return None
        else:
            for key in list(dic):
                if key_pattern == key.lower():
                    return key
            return None
    except KeyError:
        print(f'Invalid SOAP request/response.')
        return None


def parse_xml(xml_data):
    namespaces = {'urn:vertexinc:o-series:tps:7:0': 'x'}
    dict_data = xmltodict.parse(xml_data, process_namespaces=True, namespaces=namespaces)
    return dict_data


def parse_xsdfile(filename):
    namespaces = {'urn:vertexinc:o-series:tps:7:0': 'x'}
    pprint(filename)

    with open(filename, 'r') as file:
        data = file.read()
        xml_data = xmltodict.parse(data, process_namespaces=True, namespaces=namespaces)

def coalesce_str(item):
    if item is None:
        return 'null'
    else:
        return '"' + item + '"'


def coalesce_num(item):
    if item is None:
        return 'null'
    elif type(item) != int and type(item) != float:
        return 'null'
    else:
        return item


def coalesce_bool(item):
    if item is None:
        return 'null'
    elif item is True or item == 'true':
        return 'true'
    elif item is False or item == 'false':
        return 'false'
    else:
        return 'null'


def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value