import json
from pprint import pprint

import xmlschema
import os

import xmltodict

dir_path = os.path.dirname(os.path.realpath(__file__))
xml_Path = dir_path + "\\media\\"
test_file = "test1.xml"


def parse_xsdfile(filename):
    namespaces = {'urn:vertexinc:o-series:tps:7:0': 'x'}
    pprint(filename)

    with open(filename, 'r') as file:
        data = file.read()
        xml_data = xmltodict.parse(data, process_namespaces=True, namespaces=namespaces)
        # pprint(xml_data)
        # print(json.dumps(xml_data, indent=2))


def parse_xml(xml_data):
    namespaces = {'urn:vertexinc:o-series:tps:7:0': 'x'}
    dict_data = xmltodict.parse(xml_data, process_namespaces=True, namespaces=namespaces)
    # print(json.dumps(dict_data, indent=2))
    return dict_data


def get_filenames():
    files = []
    for (dirpath, dirnames, filenames) in os.walk(xml_Path):
        files.extend(filenames)
        break
    return files


def get_payload(files):
    for each_file in files:
        counter = 0
        file = open(xml_Path + each_file, 'r')
        # Read all lines in the file
        json_list = file.readlines()
        # for every row in the file
        for row in json_list:
            counter += 1
            json_doc = json.loads(row)
            # get the payload object out of the json
            payload = json_doc['payload']
            # remove the escaped double quoates
            deformatted_payload = payload.replace("\\\"", "")
            # turn the xml in to json
            new_payload = parse_xml(deformatted_payload)
            # save to a new file
            print(each_file + str(counter) + ".json")
            f = open(each_file + str(counter) + ".json", "a")
            f.write(json.dumps(new_payload, indent=2))
            f.close()


def print_filenames(files):
    for file in files:
        print(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files = get_filenames()
    get_payload(files)
    # print_filenames(files)
    # parse_xsd(xml_Path + test_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
