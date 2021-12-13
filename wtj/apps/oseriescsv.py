#
import csv

from apps.postgresql import insert_dataset, insert_data_element


def read_dataset_csv(filename):
    with open(filename, newline='') as csv_file:
        the_file = csv.reader(csv_file, quotechar='"')
        line_count = 0
        for row in the_file:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                params = [row[0], row[1], row[2], row[3], row[4]]
                insert_dataset(params)
                line_count += 1
            print(f'Processed {line_count} lines.')


def read_dataelement_csv(filename):
    with open(filename, newline='') as csv_file:
        the_file = csv.reader(csv_file, quotechar='"')
        line_count = 0
        for row in the_file:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                params = [row[0], row[1], row[2], row[3], row[4],
                          row[5], row[6], row[7], row[8], row[9], row[10]]
                insert_data_element(params)
                # print(row)
                line_count += 1
            print(f'Processed {line_count} lines.')


