from configparser import ConfigParser
import psycopg2


# Configure the PostgreSQL Connection with the config.ini file
def config(filename='config.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


# Connect to the PostgreSQL database
def test_connect():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# Get one row of data
def get_one_row(sql, parameters):
    number_parameters = len(parameters)
    conn = None
    try:
        # read connection parameters
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if number_parameters == 1:
            cur.execute(sql, (parameters[0],))
        if number_parameters == 2:
            cur.execute(sql, (parameters[0], parameters[1]))
        if number_parameters == 3:
            cur.execute(sql, (parameters[0], parameters[1], parameters[2]))
        if number_parameters == 4:
            cur.execute(sql, (parameters[0], parameters[1], parameters[2], parameters[3]))
        if number_parameters == 5:
            cur.execute(sql, (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]))
        row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return row


# insert one dataset
def put_dataset(sql, parameters):
    conn = None
    try:
        # read connection parameters
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (parameters[0], parameters[1], parameters[2], parameters[3],
                          parameters[4], parameters[5], parameters[6]))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


# insert one data element
def put_data_element(sql, parameters):
    conn = None
    try:
        # read connection parameters
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (parameters[0], parameters[1], parameters[2], parameters[3],
                          parameters[4]))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


def get_data_set(data_set_name, data_source_id, data_source_version_id, storage_instance_id,
                 storage_instance_version_id):
    params = [data_set_name, data_source_id, data_source_version_id, storage_instance_id,
              storage_instance_version_id]
    sql = 'SELECT datasetid ' \
          'from vdp_dev.dataset ' \
          'where datasetname = %s and datasourceid = %s and datasourceversionid = %s ' \
          'and storageinstanceid = %s and storageinstanceversionid = %s'
    row = get_one_row(sql, params)
    return row


def get_data_set_by_name(data_set_name):
    params = [data_set_name]
    sql = "select d.datasetid from vdp_dev.dataset d " \
          "join vdp_dev.datasourceversion dsv on dsv.datasourceid = d.datasourceid " \
          "and dsv.datasourceversionid = d.datasourceversionid " \
          "join vdp_dev.storageinstanceversion siv on siv.storageinstanceid = d.storageinstanceid " \
          "where dsv.datasourceversionname = 'O Series Database Data Models 9.0 SR4' " \
          "and siv.storageinstanceversionname = 'oseriesRPTTables.csv' " \
          "and lower(d.datasetname) = lower(%s)"
    row = get_one_row(sql, params)
    return row


def get_data_source_version(data_source_version_name):
    params = [data_source_version_name]
    sql = 'SELECT datasourceid, datasourceversionid ' \
          'from vdp_dev.datasourceversion ' \
          'where datasourceversionname = %s'
    row = get_one_row(sql, params)
    return row


def get_element_data_type(data_type_domain_name):
    params = [data_type_domain_name]
    sql = 'SELECT elementdatatypeid ' \
          'from vdp_dev.elementdatatype ' \
          'where lower(elementdatatypename) = lower(%s)'
    row = get_one_row(sql, params)
    return row


def get_data_source_domain(data_source_domain_name, data_source_id, data_source_version_id):
    params = [data_source_domain_name, data_source_id, data_source_version_id]
    sql = 'SELECT datasourcedomainid ' \
          'from vdp_dev.datasourcedomain ' \
          'where datasourcedomainname = %s and datasourceid = %s and datasourceversionid = %s'
    row = get_one_row(sql, params)
    return row


def get_storage_instance(storage_instance_name, data_source_id, data_source_version_id):
    params = [storage_instance_name, data_source_id, data_source_version_id]
    sql = 'SELECT storageinstanceid, storageinstanceversionid ' \
          'from vdp_dev.storageinstanceversion ' \
          'where storageinstanceversionname = %s and datasourceid = %s and datasourceversionid = %s'
    row = get_one_row(sql, params)
    return row


def insert_dataset(in_parameters):
    data_set_name = in_parameters[0]
    data_set_description = in_parameters[1]
    data_source_version_name = in_parameters[2]
    data_source_domain_name = in_parameters[3]
    storage_instance_version_name = in_parameters[4]
    data_source = get_data_source_version(data_source_version_name)
    data_source_domain = get_data_source_domain(data_source_domain_name, data_source[0], data_source[1])
    storage_instance = get_storage_instance(storage_instance_version_name, data_source[0], data_source[1])
    sql = 'insert into vdp_dev.dataset (datasetid, datasourceid, datasourceversionid, datasourcedomainid, ' \
          'storageinstanceid, storageinstanceversionid, datasetname, datasetdescription) ' \
          'select get_uuid(), %s, %s, %s, %s, %s, %s, %s'
    parameters = [data_source[0], data_source[1], data_source_domain[0], storage_instance[0], storage_instance[1],
                  data_set_name, data_set_description]
    put_dataset(sql, parameters)


def insert_data_element(in_parameters):
    data_set_name = in_parameters[0]
    data_element_name = in_parameters[1]
    data_type_domain_name = in_parameters[2]
    is_required_ind = in_parameters[3]
    if is_required_ind == '1':
        is_required = 'true'
    else:
        is_required = 'false'
    data_format = in_parameters[4]
    reference_data_set_name = in_parameters[5]
    min_length = in_parameters[6]
    max_length = in_parameters[7]
    data_source_version_name = in_parameters[8]
    data_source_domain_name = in_parameters[9]
    storage_instance_version_name = in_parameters[10]
    data_source = get_data_source_version(data_source_version_name)
    storage_instance = get_storage_instance(storage_instance_version_name, data_source[0], data_source[1])
    element_data_type = get_element_data_type(data_type_domain_name)
    data_set = get_data_set(data_set_name, data_source[0], data_source[1], storage_instance[0],
                            storage_instance[1])

    sql = 'insert into vdp_dev.dataelement (datasetid, dataelementid, dataelementname, dataelementdescription, ' \
          'referencedatasetid, elementdatatypeid, securitysensitiveindicator, piisensitiveindicator, ' \
          'requiredindicator, format ) ' \
          'select %s, get_uuid(), %s, %s, null, %s, false, false, ' + is_required + ', %s '
    params = [data_set[0], data_element_name, 'Column Name - ' + data_element_name, element_data_type[0],
              data_format]
    put_data_element(sql, params)

