import os
import csv
# import sys

working_file_path = os.getcwd() + "\\wtjfiles\\"
data_types_file_path = os.getcwd() + "\\media\\" + "fieldDataTypes.txt"
batch_inserts = 1000


# Format the column value according to its data type
def format_column_value(data_type, column_value):
    if len(column_value) == 0:
        formatted_value = "null"
    else:
        if (data_type is None):
            print("Data Type is None")
        if (data_type == "integer") or ("decimal" in data_type):
            formatted_value = column_value
        elif data_type == "boolean":
            if column_value == "1":
                formatted_value = "true"
            else:
                formatted_value = "false"
        else:
            formatted_value = "'" + column_value.replace("'", "''") + "'"
    return formatted_value


# Gets the data type for the provided column_name; Does a lookup in the data_types dictionary
#    using the lower case version of the column name
# returns: string - the data type
def get_column_data_type(column_name, data_types):
    the_data_type = data_types.get(column_name.lower().strip('"'))
    # print(column_name.lower().strip('"'))
    return the_data_type


# Creates the INSERT INTO part of the SQL using the column name
# returns: string - insert_sql_fragment
def set_insert_sql_fragment(column_names):
    insert_sql_fragment = "insert into wtj.rawwtj("
    for column_name in column_names:
        insert_sql_fragment += column_name + ", "
    # Trim the last comma and add the end parentheses
    return insert_sql_fragment[:-2] + ") " + "\n"


# Creates the VALUES part of the SQL
# returns: string - values_sql_fragment
def set_values_sql_fragment(column_names, column_values, data_types):
    values_sql_fragment = " ("
    # Loop thru all the column names
    for idx, column_name in enumerate(column_names):
        data_type = get_column_data_type(column_name, data_types)
        # Append the next value to the string
        values_sql_fragment += format_column_value(data_type, column_values[idx].replace("'", "''").strip('"')) + ", "
    # Trim the last comma and add the end parentheses
    return values_sql_fragment[:-2] + ") "


# Process all the rows (lines) in the WTJ file and write to a SQL file
def process_wtj_data(lines, data_types, full_wtj_filename):
    sql_filename = full_wtj_filename + ".sql"
    with open(sql_filename, 'w') as sql_file:
        line_number = 1
        for line in lines:
            # print(f'     Line #: {line_number}')
            # Create INSERT fragment
            if line_number == 1:
                column_names = line.replace('\n', '').split(",")
                insert_sql_fragment = set_insert_sql_fragment(column_names)
                line_number += 1
            else:
            # Create VALUES fragment
                if len(line.replace('\n', '')) > 0:
                    column_values = line.replace('\n', '').split(",")
                    values_sql_fragment = set_values_sql_fragment(column_names, column_values, data_types)
                    # Determine if a new SQL batch statement should start
                    sql_batch_pointer = line_number % batch_inserts
                    # End of 1000 insert batch
                    if sql_batch_pointer == 1:
                        sql_file.write(values_sql_fragment)
                        sql_file.write(";\n")
                    # Beginning of new batch
                    elif sql_batch_pointer == 2:
                        sql_file.write(insert_sql_fragment)
                        sql_file.write("values " + values_sql_fragment)
                        sql_file.write(",\n")
                    # Middle of the batch
                    else:
                        sql_file.write(values_sql_fragment)
                        sql_file.write(",\n")
                    line_number += 1
    sql_file.close()


# Read WTJ file
# returns : the file as a list of lines (list of strings)
def read_wtj_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


# Load the file that has the data type for each column
# Returns a data_types dictionary
#    - Each item in data_types has item[0] = columnname and item[1] = datatype
def get_field_data_types(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data_types = {item[0]: item[1] for item in reader}
        return data_types


# Get all WTJ file names
def get_all_wtj_file_names():
    return os.listdir(working_file_path)


if __name__ == '__main__':
    # Get a list of all the file names
    wtj_file_names = get_all_wtj_file_names()

    # Load the column data types file into a list of column,datatype pairs
    field_data_types = get_field_data_types(data_types_file_path)

    # Read WTJ file to get a list of rows (lines) from the file
    for wtj_file_name in wtj_file_names:
        print(f'Processing File: {wtj_file_name}')
        process_wtj_data(read_wtj_file(working_file_path + wtj_file_name),
                         field_data_types,
                         wtj_file_name)


# ------------------------------------------------------------------------------
# Code fragments not used
    # for file in files:
    #     if os.path.isfile(os.path.join(working_file_path, file)):
    #         print(file)
    # f = open(os.path.join(your_path, file), 'r')
    # for x in f:
    #     if keyword in x:
    # # do what you want
    # f.close()

        # lines = read_wtj_file(full_wtj_filename)
        #
        # # Process the rows (lines) of data
        # process_wtj_data(lines, data_types, full_wtj_filename)

    # if len(sys.argv) < 2:
    #     full_data_types_filename = os.getcwd() + working_file_path + data_types_file
    #     full_wtj_filename = os.getcwd() + working_file_path + wtj_file
    # else:
    #     full_data_types_filename = data_types_file
    #     full_wtj_filename = sys.argv[1]
    #
