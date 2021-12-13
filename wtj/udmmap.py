import csv

udm_path = '.\\media\\'
udm_file = 'udmmap.csv'


def parse_udm_map():
    oseries_map = []
    out_file = open(udm_path + 'insertUdm.sql', "w+")
    with open(udm_path + udm_file, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for rows in reader:
            insert_stmt = 'INSERT INTO vdp_dev.dataelementudm (' \
                          'udmid, ' \
                          'wtjcolumn, longname, tablename, notes, description, format, ussales, ' \
                          'usproc, vatsales, vatproc, esreturn, invoiceevent, invoiceperspective, facttype) ' \
                          'SELECT get_uuid(), '
            # print(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6],
            #       rows[7], rows[8], rows[9], rows[10], rows[11], rows[12], rows[13])
            insert_stmt = insert_stmt + "'" + rows[2] + "'," \
                          + "'" + rows[0] + "'," + "'" + rows[1] + "'," + "'" + rows[3] + "'," \
                          + "'" + rows[4] + "'," + "'" + rows[5] + "'," + "'" + rows[6] + "'," \
                          + "'" + rows[7] + "'," + "'" + rows[8] + "'," + "'" + rows[9] + "'," \
                          + "'" + rows[10] + "'," + "'" + rows[11] + "'," \
                          + "'" + rows[12] + "'," + "'" + rows[13] + "';"
            out_file.write(insert_stmt + "\n")
            # data_set_id = get_data_set_by_name(rows[1])
            # print(rows[0], rows[1], rows[2])
    out_file.close()


if __name__ == '__main__':
    # Load wide tax journal json file into a string
    udm_map = parse_udm_map()