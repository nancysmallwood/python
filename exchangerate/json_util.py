import json


def write_json_file(filename, json_data):
    with open(filename, 'w') as f:
        json.dump(json_data, f)


def print_json(json_data):
    json_object = json.loads(json_data)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
