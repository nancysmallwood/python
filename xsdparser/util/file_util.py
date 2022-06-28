import json
import os


def print_filenames(files):
    for file in files:
        print(file)


def get_filenames(osp_location):
    # files = []
    # for (dirpath, dirnames, filenames) in os.walk(osp_location):
    #     files.extend(filenames)
    #     break
    # return files
    for dir, dirs, files in os.walk(osp_location):
        files = [os.path.join(f) for f in files if f.endswith('.txt')]
    return files


# Returns:  string of JSON of file contents
def get_json_file(full_file_name):
    with open(full_file_name, 'r') as file:
        data = file.read().replace('\n', '')
    return json.loads(data)


# Returns:  string of JSON
def get_json(input_str):
    return json.loads(input_str)


# Returns list of lines from a file
def get_rows(full_file_name):
    with open(full_file_name) as file:
        rows = [row.rstrip() for row in file]
        return rows


def print_filenames(files):
    for file in files:
        print(file)
