# Read wtj json file and load into table for analysis
import csv
import json

# json spec location
from apps.postgresql import get_element_data_type, get_data_set_by_name

wtj_path = '.\\media\\'
wtj_file = 'wtj_columns.json'
# wtj_file = 'test.json'
mapFileName = 'ColsToDataSets2.txt'
output_sql_file = 'dataelements.sql'
output_csv_file = 'wtj_columns.csv'
output_json_file = 'wtj_openapi3.json'


# MAPPING OF tags to OSeries tables to dataset ids-----------------------------------------------
class OSeriesMapItem:
    def __init__(self, tag, table_name, data_set_id):
        self.tag = tag
        self.table_name = table_name
        self.data_set_id = data_set_id

    def __str__(self):
        return f'MapItem - tag: {self.tag}, ' \
               f'table_name: {self.table_name}, ' \
               f'data_set_id: {self.data_set_id} '


def get_data_set_id(table_map, tag):
    data_set_id = None
    for item in table_map:
        if item.tag.lower() == tag.lower():
            data_set_id = item.data_set_id
    return data_set_id


def get_data_set_id_from_query_cols(table_map, json_object):
    data_set_id = None
    for json_column in json_object:
        if 'oVersion' in json_column:
            if json_column['oVersion'] == '8.0':
                if json_column['column'] is not None:
                    clean_column_name = clean(json_column['column'])
                    for item in table_map:
                        if item.tag.lower() == clean_column_name.lower():
                            data_set_id = item.data_set_id
    return data_set_id


def get_dataset_name_from_dict(columnName, table_dict):
    clean_column_name = clean(columnName).lower()
    for key in table_dict:
        if clean_column_name == key.lower():
            # print(clean(columnName).lower() + ' -- ' + key)
            return table_dict[key]
    return 'Nope'


def clean(columnName):
    new_col_name = columnName
    best_col_name = columnName
    if columnName.find('.') != -1:
        new_col_name = columnName.rpartition('.')[0]
        best_col_name = new_col_name
    if new_col_name.find(',') != -1:
        new_col_name = new_col_name.rpartition(',')[0]
        best_col_name = new_col_name
    return best_col_name


def list_to_string(the_list):
    new_string = '['
    for item in the_list:
        new_string = new_string + '\'' + item + '\','
    new_string = new_string.rstrip(new_string[-1]) + ']'
    return new_string


#
# class OSeriesMap:
#     def __init__(self):
#         self.map = []
#
#     def add(self, item):
#         self.map.append(item)


# Query to INSERT element -----------------------------------------------
# Class to build an insert statement for each wtf column
class QueryColumn:
    def __init__(self):
        self.oVersion = ''
        self.columnName = ''


class Query:
    def __init__(self):
        self.query_columns = 'insert into vdp_dev.dataelement(datasetid, dataelementid, securitySensitiveIndicator, ' \
                             'piiSensitiveIndicator, requiredIndicator,'
        self.query_values = "values ('e8094819-68a0-c2e4-d32d-370e91e4dea8', get_uuid(), false, " \
                            "false, false, "
        self.elementName = ''
        self.list_query_columns = []

#
# # Create an individual column
def build_column(json_column, map):
    query = Query()

    if 'queryCols' in json_column and 'queryCol' not in json_column:
        if json_column['queryCols'] is not None:
            for item in json_column['queryCols']:
                q = QueryColumn()
                if 'oVersion' in item:
                    q.oVersion = item['oVersion']
                if 'column' in item:
                    q.columnName = item['column']
                    q.columnName = q.columnName.replace("'", "''")
                query.list_query_columns.append(q)

    if 'name' in json_column:
        query.query_columns = query.query_columns + 'dataelementname,'
        query.query_values = query.query_values + "'" + json_column['name'] + "',"
        # use the name as the description for now
        query.query_columns = query.query_columns + 'dataelementdescription,'
        query.query_values = query.query_values + "'" + json_column['name'] + "',"
        query.elementName = json_column['name']

    if 'type' in json_column:
        element_data_type = get_element_data_type(json_column['type'])
        query.query_columns = query.query_columns + 'elementdatatypeid,'
        query.query_values = query.query_values + "'" + element_data_type[0] + "',"

    # Indicators
    if 'nullable' in json_column:
        query.query_columns = query.query_columns + 'nullableIndicator,'
        if json_column['nullable']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'nullableIndicator,'
        query.query_values = query.query_values + "false,"

    if 'encode' in json_column:
        query.query_columns = query.query_columns + 'encodedIndicator,'
        if json_column['encode']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'encodedIndicator,'
        query.query_values = query.query_values + "false,"

    if 'random' in json_column:
        query.query_columns = query.query_columns + 'randomIndicator,'
        if json_column['random']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'randomIndicator,'
        query.query_values = query.query_values + "false,"

    if 'uuid' in json_column:
        query.query_columns = query.query_columns + 'uuidIndicator,'
        if json_column['uuid']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'uuidIndicator,'
        query.query_values = query.query_values + "false,"

    if 'queryCol' in json_column:
        queryCol = json_column['queryCol']
        if queryCol is not None:
            data_set_id = get_data_set_id(map, clean(queryCol))
            if data_set_id is not None:
                query.query_columns = query.query_columns + 'referencedatasetid,'
                query.query_values = query.query_values + "'" + data_set_id + "',"
            query.query_columns = query.query_columns + 'queryCol,'
            queryCol = queryCol.replace("'", "''")
            query.query_values = query.query_values + "'" + queryCol + "',"

    if 'pattern' in json_column:
        query.query_columns = query.query_columns + 'pattern,'
        query.query_values = query.query_values + "'" + json_column['pattern'] + "',"

    if 'column' in json_column:
        query.query_columns = query.query_columns + 'columnName,'
        query.query_values = query.query_values + "'" + json_column['column'] + "',"

    if 'minAmount' in json_column:
        query.query_columns = query.query_columns + 'minAmount,'
        query.query_values = query.query_values + str(json_column['minAmount']) + ","

    if 'maxAmount' in json_column:
        query.query_columns = query.query_columns + 'maxAmount,'
        query.query_values = query.query_values + str(json_column['maxAmount']) + ","

    if 'minId' in json_column:
        query.query_columns = query.query_columns + 'minId,'
        query.query_values = query.query_values + str(json_column['minId']) + ","

    if 'maxId' in json_column:
        query.query_columns = query.query_columns + 'maxId,'
        query.query_values = query.query_values + str(json_column['maxId']) + ","

    if 'minDate' in json_column:
        query.query_columns = query.query_columns + 'minDate,'
        query.query_values = query.query_values + str(json_column['minDate']) + ","

    if 'maxDate' in json_column:
        query.query_columns = query.query_columns + 'maxDate,'
        query.query_values = query.query_values + str(json_column['maxDate']) + ","

    if 'notes' in json_column:
        query.query_columns = query.query_columns + 'notes,'
        query.query_values = query.query_values + "'" + json_column['notes'] + "',"

    if 'nullRate' in json_column:
        query.query_columns = query.query_columns + 'nullRate,'
        query.query_values = query.query_values + str(json_column['nullRate']) + ","

    if 'oVersion' in json_column:
        query.query_columns = query.query_columns + 'oVersion,'
        query.query_values = query.query_values + "'" + json_column['oVersion'] + "',"

    if 'options' in json_column:
        query.query_columns = query.query_columns + 'options,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['options']) + ","

    if 'columns' in json_column:
        query.query_columns = query.query_columns + 'columnNames,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['columns']) + ","

    if 'samples' in json_column:
        query.query_columns = query.query_columns + 'samples,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['samples']) + ","

    if 'repeatPct' in json_column:
        query.query_columns = query.query_columns + 'repeatPct,'
        query.query_values = query.query_values + str(json_column['repeatPct']) + ","

    if 'wtjVersion' in json_column:
        query.query_columns = query.query_columns + 'wtjVersion,'
        query.query_values = query.query_values + "'" + json_column['wtjVersion'] + "',"

    query.query_columns = query.query_columns.rstrip(query.query_columns[-1]) + ')'
    query.query_values = query.query_values.rstrip(query.query_values[-1]) + ');'
    return query


# # Create an individual column
# csv row name, type, nullable, uuid, notes, oversion, wtjversion
def build_csv_row(json_column):
    csv_row = ""

    if 'name' in json_column:
        if json_column['name'] is not None:
            csv_row = csv_row + '"' + json_column['name'] + '",'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    if 'type' in json_column:
        if json_column['type'] is not None:
            csv_row = csv_row + '"' + json_column['type'] + '",'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    # Indicators
    if 'nullable' in json_column:
        if json_column['nullable'] is not None:
            if json_column['nullable'] is True:
                csv_row = csv_row + '1,'
            else:
                csv_row = csv_row + '0,'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    if 'uuid' in json_column:
        if json_column['uuid'] is not None:
            if json_column['uuid'] is True:
                csv_row = csv_row + '1,'
            else:
                csv_row = csv_row + '0,'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    if 'notes' in json_column:
        if json_column['notes'] is not None:
            csv_row = csv_row + '"' + json_column['notes'] + '",'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    if 'oVersion' in json_column:
        if json_column['oVersion'] is not None:
            csv_row = csv_row + '"' + json_column['oVersion'] + '",'
        else:
            csv_row = csv_row + ','
    else:
        csv_row = csv_row + ','

    if 'wtjVersion' in json_column:
        if json_column['wtjVersion'] is not None:
            csv_row = csv_row + '"' + json_column['wtjVersion'] + '"'

    return csv_row


# PARSE -----------------------------------------------------------------
# # parse the json string and process each column
def parse_wtj_columns_and_write(wtj_json_str, map):
    if 'columns' in wtj_json_str:
        out_file = open(wtj_path + output_sql_file, "w+")
        for json_column in wtj_json_str['columns']:
            # print(json_column)
            query = build_column(json_column, map)
            out_file.write(query.query_columns + "\n")
            out_file.write(query.query_values + "\n")
            for item in query.list_query_columns:
                q = "insert into vdp_dev.DataElementQueryCol(datasetid, dataelementid, queryColId,oVersion,columnName) " \
                    "select 'e8094819-68a0-c2e4-d32d-370e91e4dea8', dataelementid, get_uuid(), " \
                    "'" + item.oVersion + "','" + item.columnName + "' from vdp_dev.DataElement " \
                                                                    "where dataelementname = '" + query.elementName + "' " \
                                                                                                                      "and datasetid = 'e8094819-68a0-c2e4-d32d-370e91e4dea8';"
                out_file.write(q + "\n")
            # print(query.query_columns)
            # print(query.query_values)
        out_file.close()


def parse_wtj_columns(wtj_json_str):
    if 'columns' in wtj_json_str:
        out_file = open(wtj_path + output_csv_file, "w+")
        out_file.write("name, type, nullable, uuid, notes, oversion, wtjversion\n")
        for json_column in wtj_json_str['columns']:
            # print(json_column)
            csv_row = build_csv_row(json_column)
            out_file.write(csv_row + "\n")
            # print(csv_row)
            # query = build_column(json_column, map)
            # out_file.write(query.query_columns + "\n")
            # out_file.write(query.query_values + "\n")
            # for item in query.list_query_columns:
            #     q = "insert into vdp_dev.DataElementQueryCol(datasetid, dataelementid, queryColId,oVersion,columnName) " \
            #         "select 'e8094819-68a0-c2e4-d32d-370e91e4dea8', dataelementid, get_uuid(), " \
            #         "'" + item.oVersion + "','" + item.columnName + "' from vdp_dev.DataElement " \
            #                                                         "where dataelementname = '" + query.elementName + "' " \
            #                                                                                                           "and datasetid = 'e8094819-68a0-c2e4-d32d-370e91e4dea8';"
            #     out_file.write(q + "\n")
            # print(query.query_columns)
            # print(query.query_values)
        out_file.close()


# Method to load database table aliases and match them with table names
def load_data_set_map():
    with open(wtj_path + mapFileName, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        table_dict = {rows[0]: rows[1] for rows in reader}
    return table_dict

# Create an individual column
def build_json_column(json_column):
    query = Query()

    if 'queryCols' in json_column and 'queryCol' not in json_column:
        if json_column['queryCols'] is not None:
            for item in json_column['queryCols']:
                q = QueryColumn()
                if 'oVersion' in item:
                    q.oVersion = item['oVersion']
                if 'column' in item:
                    q.columnName = item['column']
                    q.columnName = q.columnName.replace("'", "''")
                query.list_query_columns.append(q)

    if 'name' in json_column:
        query.query_columns = query.query_columns + 'dataelementname,'
        query.query_values = query.query_values + "'" + json_column['name'] + "',"
        # use the name as the description for now
        query.query_columns = query.query_columns + 'dataelementdescription,'
        query.query_values = query.query_values + "'" + json_column['name'] + "',"
        query.elementName = json_column['name']

    if 'type' in json_column:
        element_data_type = get_element_data_type(json_column['type'])
        query.query_columns = query.query_columns + 'elementdatatypeid,'
        query.query_values = query.query_values + "'" + element_data_type[0] + "',"

    # Indicators
    if 'nullable' in json_column:
        query.query_columns = query.query_columns + 'nullableIndicator,'
        if json_column['nullable']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'nullableIndicator,'
        query.query_values = query.query_values + "false,"

    if 'encode' in json_column:
        query.query_columns = query.query_columns + 'encodedIndicator,'
        if json_column['encode']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'encodedIndicator,'
        query.query_values = query.query_values + "false,"

    if 'random' in json_column:
        query.query_columns = query.query_columns + 'randomIndicator,'
        if json_column['random']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'randomIndicator,'
        query.query_values = query.query_values + "false,"

    if 'uuid' in json_column:
        query.query_columns = query.query_columns + 'uuidIndicator,'
        if json_column['uuid']:
            query.query_values = query.query_values + "true,"
        else:
            query.query_values = query.query_values + "false,"
    else:  # default
        query.query_columns = query.query_columns + 'uuidIndicator,'
        query.query_values = query.query_values + "false,"

    if 'queryCol' in json_column:
        queryCol = json_column['queryCol']
        if queryCol is not None:
            data_set_id = get_data_set_id(map, clean(queryCol))
            if data_set_id is not None:
                query.query_columns = query.query_columns + 'referencedatasetid,'
                query.query_values = query.query_values + "'" + data_set_id + "',"
            query.query_columns = query.query_columns + 'queryCol,'
            queryCol = queryCol.replace("'", "''")
            query.query_values = query.query_values + "'" + queryCol + "',"

    if 'pattern' in json_column:
        query.query_columns = query.query_columns + 'pattern,'
        query.query_values = query.query_values + "'" + json_column['pattern'] + "',"

    if 'column' in json_column:
        query.query_columns = query.query_columns + 'columnName,'
        query.query_values = query.query_values + "'" + json_column['column'] + "',"

    if 'minAmount' in json_column:
        query.query_columns = query.query_columns + 'minAmount,'
        query.query_values = query.query_values + str(json_column['minAmount']) + ","

    if 'maxAmount' in json_column:
        query.query_columns = query.query_columns + 'maxAmount,'
        query.query_values = query.query_values + str(json_column['maxAmount']) + ","

    if 'minId' in json_column:
        query.query_columns = query.query_columns + 'minId,'
        query.query_values = query.query_values + str(json_column['minId']) + ","

    if 'maxId' in json_column:
        query.query_columns = query.query_columns + 'maxId,'
        query.query_values = query.query_values + str(json_column['maxId']) + ","

    if 'minDate' in json_column:
        query.query_columns = query.query_columns + 'minDate,'
        query.query_values = query.query_values + str(json_column['minDate']) + ","

    if 'maxDate' in json_column:
        query.query_columns = query.query_columns + 'maxDate,'
        query.query_values = query.query_values + str(json_column['maxDate']) + ","

    if 'notes' in json_column:
        query.query_columns = query.query_columns + 'notes,'
        query.query_values = query.query_values + "'" + json_column['notes'] + "',"

    if 'nullRate' in json_column:
        query.query_columns = query.query_columns + 'nullRate,'
        query.query_values = query.query_values + str(json_column['nullRate']) + ","

    if 'oVersion' in json_column:
        query.query_columns = query.query_columns + 'oVersion,'
        query.query_values = query.query_values + "'" + json_column['oVersion'] + "',"

    if 'options' in json_column:
        query.query_columns = query.query_columns + 'options,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['options']) + ","

    if 'columns' in json_column:
        query.query_columns = query.query_columns + 'columnNames,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['columns']) + ","

    if 'samples' in json_column:
        query.query_columns = query.query_columns + 'samples,'
        query.query_values = query.query_values + "ARRAY" + list_to_string(json_column['samples']) + ","

    if 'repeatPct' in json_column:
        query.query_columns = query.query_columns + 'repeatPct,'
        query.query_values = query.query_values + str(json_column['repeatPct']) + ","

    if 'wtjVersion' in json_column:
        query.query_columns = query.query_columns + 'wtjVersion,'
        query.query_values = query.query_values + "'" + json_column['wtjVersion'] + "',"

    query.query_columns = query.query_columns.rstrip(query.query_columns[-1]) + ')'
    query.query_values = query.query_values.rstrip(query.query_values[-1]) + ');'
    return query


# PARSE -----------------------------------------------------------------
# parse the json string and process each column
# def parse_wtj_columns_and_write_json(wtj_json_str):
#     if 'columns' in wtj_json_str:
#         out_file = open(wtj_path + output_json_file, "w+")
#         for json_column in wtj_json_str['columns']:
#             print(json_column + "\n")
#             new_json_column = build_json_column(json_column)
#             out_file.write(new_json_column + "\n")
#             # out_file.write(q + "\n")
#         out_file.close()


# # Method to load database table aliases and match them with table names
def get_data_set_map():
    oseries_map = []
    with open(wtj_path + mapFileName, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for rows in reader:
            # data_set_id = get_data_set_by_name(rows[1])
            oseries_map.append(OSeriesMapItem(rows[0], rows[1], rows[2]))
            # print(rows[0], rows[1], rows[2])
    return oseries_map


# FILE LOADING METHODS -----------------------------------------------------------------
# Read the Wide Tax Journal file into a string
# Send to the method to create DataSets
def parse_wtj_file():
    with open(wtj_path + wtj_file, 'r') as file:
        data = file.read().replace('\n', '')
    return json.loads(data)


def create_sql():
    # Load wide tax journal json file into a string
    wtj_json = parse_wtj_file()
    # # Load the field -> database column map into a dictionary
    oseries_map = get_data_set_map()
    # # Parse the json string and process each column
    parse_wtj_columns_and_write(wtj_json, oseries_map)


def create_other():
    # Load wide tax journal json file into a string
    wtj_json = parse_wtj_file()
    # parse_wtj_columns_and_write_json(wtj_json)
    print(wtj_json)


def wtj_json_spec_to_csv():
    # Load wide tax journal json file into a string
    wtj_json = parse_wtj_file()
    parse_wtj_columns(wtj_json)
    # print(wtj_json)


# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    wtj_json_spec_to_csv()
