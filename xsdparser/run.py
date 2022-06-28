import json
from json import JSONDecodeError

from osplogs import get_message_type
from parse.soapparse import get_json_payload, get_payload
from util.dictionary_util import xml_to_dict, clean_nones
from util.file_util import get_filenames, get_rows


def process_row(row, filename, row_number):
    try:
        # Read line as JSON
        osp_json = json.loads(row.rstrip())

        # Add a JSON element for the source file
        osp_new = {"ospSource": {"file": filename, "row": row_number, "messageType": ""}}

        # Load raw JSON row into a string
        osp_new.update(osp_json)

        # Convert "payload" XML to a dictionary
        payload_raw = xml_to_dict(osp_new['payload'])

        # get the JSON version of the XML payload
        payload_json = get_json_payload(get_payload(payload_raw))

        # Update original payload (the XML version) with the JSON version
        if payload_json is not None:
            # new_osp['payload'] = clean_nones(json.loads(payload_json))
            osp_new['payload'] = json.loads(payload_json)
            # Get and set the message type, e.g. InvoiceResponse
            osp_new['ospSource']['messageType'] = get_message_type(osp_new['payload'])
            # Remove None or null items
            osp_clean = clean_nones(osp_new)
            f = open(filename + str(row_number) + ".json", "w")
            # f.write(json.dumps(json.loads(json_payload), indent=2))
            f.write(json.dumps(osp_clean, indent=2))
            f.close()
    except (JSONDecodeError, json.JSONDecodeError, ValueError):
        pass


def process_file(filename):
    print(filename)
    rows = get_rows(filename)
    row_number = 0
    for row in rows:
        row_number += 1
        # if row_counter == 100:
        process_row(row, filename, row_number)


def run(filepath):
    files = get_filenames(filepath)
    for filename in files:
        process_file(filepath + filename)


# ------------------------------------------------------------
if __name__ == '__main__':
    request_path = "C:\\temp\\osplogs\\request\\"
    response_path = "C:\\temp\\osplogs\\response\\"
    test_path = "C:\\temp\\osplogs\\test\\"
    run(test_path)
    # run(request_path)
    # run(response_path)
