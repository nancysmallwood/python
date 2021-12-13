from configparser import ConfigParser
import psycopg2


# Configure the PostgreSQL Connection with the config.ini file
def config(filename='database.properties', section='postgresql'):
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


# Test Connect to the PostgreSQL database
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


def get_db_connection():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print('Database connection open.')
    return conn


def commit_and_close_db_connection(conn):
    if conn is not None:
        conn.commit()
        conn.close()
        print('Database connection closed.')
    else:
        print('Database connection was not open.')


def close_db_without_commit(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed without committing transactions.')
    else:
        print('Database connection was not open.')


# Insert s3 filename and number of rows
def insert_s3_file(file_name, number_of_rows):
    sql = "insert into wtj.wtjfile(fileid, filename, numrows) select get_uuid()," \
          "%s, %s"
    try:
        # read connection parameters
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (file_name, number_of_rows))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


# def get_file_id(file_name):
#     sql = "select fileid from wtj.wtjfile where filename = %s"
#     try:
#         # read connection parameters
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(sql, (file_name,))
#         fileid = cur.fetchone()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         return None
#     finally:
#         if conn is not None:
#             conn.commit()
#             conn.close()
#     return fileid


# Get fileId which will be UUID
def get_file_id(conn, file_name):
    fileid = None
    sql = "select fileid from wtj.wtjfile where filename = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (file_name,))
        fileid = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return fileid[0]


# Populate all the datatypes to keep in memory for efficiency
def get_field_data_types(conn):
    sql = "select fieldname, datatypename from wtj.wtjfielddatatype"
    cur = conn.cursor()
    cur.execute(sql)
    field_data_types = cur.fetchall();
    return field_data_types


def start_file_load_process(conn, fileid):
    isql = "insert into wtj.wtjfileloadstatus(fileid, processstart) select %s, current_timestamp"
    dsql = "delete from wtj.wtjfileloadstatus where fileid = %s"

    cur = conn.cursor()
    cur.execute(dsql, fileid)
    cur.execute(isql, fileid)


def get_field_data_type(field_name, field_data_types):
    data_type = None
    for i in range(len(field_data_types)):
        # print(field_data_types[i]) # - the tuple
        # print(field_data_types[i][0]) # - first field
        # print(field_data_types[i][1]) # - second field
        if field_data_types[i][0].lower() == field_name.lower():
            data_type = field_data_types[i][1]
    return data_type


# each field is one of five data types - integer, boolean,  decimal
#    timestamp or varchar. This method formats the value for the
#    insert statement
def get_formatted_field_value_for_sql(value, data_type):
    if (data_type == 'integer') or (data_type == 'decimal'):
        return str(value)
    elif data_type == 'boolean':
        if (value == True) or (value == 1):
            return 'true'
        else:
            return 'false'
    elif (data_type == 'varchar') or (data_type == 'timestamp'):
        return "'" + str(value).replace("'","''").replace("%","\%") + "'"


# Insert ONE row of WTJ data
def insert_wtj_row(conn, fileid, field_names, items, field_data_types):
    isql = 'insert into wtj.wtjdata(fileid,'
    ssql = 'select ' + "'" + fileid + "',"
    # Get the file id

    if len(field_names) != len(items):
        print('very bad error - field name to item mismatch')
    else:
        for i in range(len(field_names)):
            data_type = get_field_data_type(field_names[i], field_data_types)
            if (items[i] is not None) and (items[i] != ''):
                ssql = ssql + get_formatted_field_value_for_sql(items[i], data_type) + ','
                isql = isql + field_names[i] + ','
    # Trim off the last char of each string, put them together and execute
    sql = isql[:-1] + ') ' + ssql[:-1]

    try:
        cur = conn.cursor()
        cur.execute(sql)
    except (Exception, psycopg2.DatabaseError) as error:
        print('something bad happened inserting row')
        print(sql)
        print(error)
        return -1

    return 0
    # print(sql)
