# Read wtj json file and load into table for analysis
import json
import csv

orc_path = '.\\media\\'
orc_file = 'orc_columns.json'
orv_csv = 'orc_columns.csv'


# FILE LOADING METHODS -----------------------------------------------------------------
# Read the ORC file into a string
# Send to the method to create DataSets
def parse_athena_table_file():
    with open(orc_path + orc_file, 'r') as file:
        data = file.read().replace('\n', '')
    return json.loads(data)


# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    # Load wide tax journal json file into a string
    schema_json = parse_athena_table_file()
    # print(schema_json)
    # print(((schema_json['StorageDescriptor'])['cols'])['FieldSchema'])
    # Load the field -> database column map into a dictionary
    # oseries_map = get_data_set_map()
    # Parse the json string and process each column
    # parse_wtj_columns_and_write(wtj_json, oseries_map)
    with open(orc_path + orv_csv, 'w') as csvfile:
        # creating a csv writer object
        # csvwriter = csv.writer(csvfile)
        fields = ['name', 'type', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(((schema_json['StorageDescriptor'])['cols'])['FieldSchema'])
        # csvwriter.writerow(fields)
        # for item in ((schema_json['StorageDescriptor'])['cols'])['FieldSchema']:
        #     # print(item)
        #     name = item['name'].replace('\n', '')
        #     type = item['type'].replace('\n', '')
        #     comment = item['comment'].replace('\n', '')
        #     row = [name, type, comment]
        #     csvwriter.writerow(row)


