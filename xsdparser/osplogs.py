import json
from pprint import pprint

import xmltodict

from util.dictionary_util import xml_to_dict
from soapparse import get_payload, get_json_payload, get_json_payload2
from util.file_util import get_lines, get_filenames

request_path = "C:\\temp\\osplogs\\"
response_path = "C:\\temp\\osplogs\\response\\"


def run3(osp_location):
    files = get_filenames(osp_location)
    for file in files:
        print(file)
        lines = get_lines(osp_location + file)
        row_counter = 0
        for line in lines:
            row_counter += 1
            # Load raw JSON row into a string
            json_doc = json.loads(line.rstrip())
            # Get 'payload' XML object from the JSON and convert to a dictionary
            raw_payload = xml_to_dict(json_doc['payload'])
            # test = json.dumps(get_payload_object(raw_payload))
            # print(test)
            # get the JSON version of the XML
            #json_payload = get_json_payload(get_payload(raw_payload))
            json_payload = get_json_payload2(get_payload(raw_payload))
            # Update original payload (the XML version) with the JSON version
            if json_payload is not None:
                json_doc['payload'] = json.loads(json_payload)
                f = open(osp_location + file + str(row_counter) + ".json", "w")
                #f.write(json.dumps(json.loads(json_payload), indent=2))
                f.write(json.dumps(json_doc, indent=2))
                f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_path = "C:\\githubrepos\\python\\xsdparser\\media\\"
    # request_path
    # response_path
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

#def run2(osp_location):
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