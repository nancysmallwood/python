import json
from pprint import pprint

import xmltodict

from util.dictionary_util import xml_to_dict
from osp import Osp
from soapparse import get_payload, get_login, get_application_data, get_quote
from util.file_util import get_lines, get_filenames

osp_path = "C:\\temp\\osplogs\\"


def run(osp_location):
    files = get_filenames(osp_location)
    # print_filenames(files)
    for file in files:
        # print(file)
        lines = get_lines(osp_location + file)
        row_counter = 0
        for line in lines:
            row_counter += 1
            json_doc = json.loads(line.rstrip())
            osp = Osp(json_doc)
            print(osp)
            dictionary = xml_to_dict(osp.payload)
            if get_payload(dictionary) is not None:
                payload_dictionary = get_payload(dictionary)
                osp.login = get_login(payload_dictionary)
                osp.application_data = get_application_data(payload_dictionary)
                if osp.message_type == 'QUO':
                    osp.quote = get_quote(payload_dictionary)
            print(osp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run(osp_path)

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
