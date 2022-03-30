import xmltodict


def xml_to_dict(payload):
    return xmltodict.parse(payload)


# Get the Dictionary item by key name
# Returns 0 if key does not exist
def get_dic_item(dic, key_name):
    try:
        if dic is None or key_name is None:
            return None
        item = dic[key_name]
        return item
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
