import json
from pprint import pprint

import xmlschema
import os

import xmltodict

osp_path = "C:\\temp\\osplogs\\"


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


def get_filenames(osp_location):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(osp_path):
        files.extend(filenames)
        break
    return files


def get_payload(osp_location, files):
    for each_file in files:
        counter = 0
        file = open(osp_path + each_file, 'r')
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
            print(osp_location + each_file + str(counter) + ".json")
            f = open(osp_location + each_file + str(counter) + ".json", "a")
            f.write(json.dumps(new_payload, indent=2))
            f.close()


def print_filenames(files):
    for file in files:
        print(file)


def run(osp_location):
    files = get_filenames(osp_location)
    print_filenames(files)
    get_payload(osp_location, files)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run(osp_path)

