import json
from json import JSONDecodeError

from util.dictionary_util import xml_to_dict, get_dic_key, get_dic_item
from parse.soapparse import get_payload, get_json_payload
from util.file_util import get_rows, get_filenames


# TaxAreaResponse
# QuotationResponse
# InvoiceResponse
# QuotationRequest
# TaxAreaRequest
# InvoiceRequest
def get_message_type(dic):
    if get_dic_key(dic, 'message_type') is not None:
        message_type = get_dic_item(dic, get_dic_key(dic, 'message_type'))
        if message_type == 'invoicerequest':
            return 'InvoiceRequest'
        elif message_type == 'quotationresponse':
            return 'QuotationResponse'
        elif message_type == 'taxarearesponse':
            return 'TaxAreaResponse'
        elif message_type == 'invoicerequest':
            return 'InvoiceRequest'
        elif message_type == 'quotationrequest':
            return 'QuotationRequest'
        elif message_type == 'taxarearequest':
            return 'TaxAreaRequest'
        else:
            return ""
    else:
        return ""


def run3(osp_location):
    files = get_filenames(osp_location)
    for file in files:
        print(file)
        lines = get_rows(osp_location + file)
        row_counter = 0
        for line in lines:
            row_counter += 1
            # if row_counter == 100:
            try:
                # Read line as JSON
                osp_raw = json.loads(line.rstrip())

                # Add a JSON element for the source file
                osp_source = {"ospSource": {"file": file,"row": row_counter,"messageType": ""}}

                # Load raw JSON row into a string
                osp_source.update(osp_raw)

                # Convert "payload" XML to a dictionary
                payload_raw = xml_to_dict(osp_source['payload'])

                # get the JSON version of the XML payload
                payload_json = get_json_payload(get_payload(payload_raw))

                # Update original payload (the XML version) with the JSON version
                if payload_json is not None:
                    osp_source['payload'] = json.loads(payload_json)
                    # Get and set the message type, e.g. InvoiceResponse
                    osp_source['ospSource']['messageType'] = get_message_type(osp_source['payload'])
                    f = open(osp_location + file + str(row_counter) + ".json", "w")
                    # f.write(json.dumps(json.loads(json_payload), indent=2))
                    f.write(json.dumps(osp_source, indent=2))
                    f.close()
            except (JSONDecodeError, json.JSONDecodeError, ValueError):
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_path = "C:\\githubrepos\\python\\xsdparser\\media\\"
    request_path = "C:\\temp\\osplogs\\request\\test\\"
    request_test_path = "C:\\temp\\osplogs\\request\\test\\"
    response_path = "C:\\temp\\osplogs\\response\\"
    # request_path
    # response_path
    run3(request_test_path)
    run3(response_path)

# def get_filenames(osp_location):
#     files = []
#     for (dirpath, dirnames, filenames) in os.walk(osp_path):
#         files.extend(filenames)
#         break
#     return files
#
#
# def get_payload(osp_location, files):
#     for each_file in files:
#         counter = 0
#         file = open(osp_path + each_file, 'r')
#         # Read all lines in the file
#         json_list = file.readlines()
#         # for every row in the file
#         for row in json_list:
#             counter += 1
#             json_doc = json.loads(row)
#             # get the payload object out of the json
#             payload = json_doc['payload']
#             # remove the escaped double quoates
#             deformatted_payload = payload.replace("\\\"", "")
#             # turn the xml in to json
#             new_payload = parse_xml(deformatted_payload)
#             # save to a new file
#             print(osp_location + each_file + str(counter) + ".json")
#             f = open(osp_location + each_file + str(counter) + ".json", "a")
#             f.write(json.dumps(new_payload, indent=2))
#             f.close()

# def run2(osp_location):
# files = get_filenames(osp_location)
# # print_filenames(files)
# for file in files:
#     # print(file)
#     lines = get_lines(osp_location + file)
#     row_counter = 0
#     for line in lines:
#         row_counter += 1
#         json_doc = json.loads(line.rstrip())
#         dictionary = xml_to_dict(json_doc['payload'])
#         payload_dictionary = get_payload(dictionary)
#         json_doc.update(payload_dictionary)
#         # print(json_doc)
#         print(osp_location + file + str(row_counter) + ".json")
#         f = open(osp_location + file + str(row_counter) + ".json", "a")
#         f.write(json.dumps(json_doc, indent=2))
#         f.close()


# def run(osp_location):
#     files = get_filenames(osp_location)
#     # print_filenames(files)
#     for file in files:
#         # print(file)
#         lines = get_lines(osp_location + file)
#         row_counter = 0
#         for line in lines:
#             row_counter += 1
#             json_doc = json.loads(line.rstrip())
#             osp = Osp(json_doc)
#             print(osp)
#             dictionary = xml_to_dict(osp.payload)
#             if get_payload(dictionary) is not None:
#                 payload_dictionary = get_payload(dictionary)
#                 osp.login = get_login(payload_dictionary)
#                 osp.application_data = get_application_data(payload_dictionary)
#                 if osp.message_type == 'QUO':
#                     osp.quote = get_quote(payload_dictionary)
#             print(json.dumps(osp))
# def get_message_type(dic):
#     if get_dic_key(dic, 'messagetype') is not None:
#         osp_message_type = get_dic_item(dic, get_dic_key(dic, 'messagetype'))
#         if osp_message_type is None:
#             return None
#         elif osp_message_type == "QUO":
#             return "Quotation"
#         elif osp_message_type == "INV":
#             return "Invoice"
#         elif osp_message_type == "ADDR":
#             return "Tax Area Lookup"
#         else:
#             return "Unknown"

