# Read wtj json file and load into table for analysis
import json

wtj_path = '.\\media\\'
wtj_file = 'wtj_columns.json'
output_csv_file = 'wtj_columns.csv'


# Construct a CSV string from a JSON object
# Parameter: JSON string of one WTJ field
# Return:    String representing a CSV row
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


# Write CSV file
# Header row = row name, type, nullable, uuid, notes, oversion, wtjversion
# Parameter:  JSON string of all "columns" in WTJ spec
def write_wtj_csv(wtj_json_str):
    if 'columns' in wtj_json_str:
        out_file = open(wtj_path + output_csv_file, "w+")
        out_file.write("name, type, nullable, uuid, notes, oversion, wtjversion\n")
        for json_column in wtj_json_str['columns']:
            csv_row = build_csv_row(json_column)
            out_file.write(csv_row + "\n")
        out_file.close()


# Read the Wide Tax Journal file into a string
# Returns:  string of JSON file contents
def parse_wtj_file():
    with open(wtj_path + wtj_file, 'r') as file:
        data = file.read().replace('\n', '')
    return json.loads(data)


# MAIN -----------------------------------------------------------------
if __name__ == '__main__':
    wtj_json = parse_wtj_file()
    write_wtj_csv(wtj_json)
