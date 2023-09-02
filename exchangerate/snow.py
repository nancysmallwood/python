import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization


def snow_connect():
    with open(os.environ['SNOWFLAKE_PRIVATE_KEY_PATH'], "rb") as key:
        p_key = serialization.load_pem_private_key(
            key.read(),
            password=os.environ['SNOWFLAKE_PRIVATE_KEY_PASSPHRASE'].encode(),
            backend=default_backend()
        )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    conn = snowflake.connector.connect(
        user=os.environ['SNOWFLAKE_USER'],
        account=os.environ['SNOWFLAKE_ACCOUNT'],
        private_key=pkb,
        warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
        database=os.environ['SNOWFLAKE_DATABASE'],
        schema=os.environ['SNOWFLAKE_SCHEMA']
    )

    # cs = conn.cursor()
    return conn.cursor()

def snow_insert_rates(date_str, rates_dict):
    from exchangerate.snow import snow_connect
    cur = snow_connect()
    # open json
    # for every k,v in "rates", insert key as currencycode and value as the rate
    for k in rates_dict.keys():
        # print("key = " + k + "  value = " + str(rates.get(k)))
        sql = "INSERT INTO DB_DEV_EVENTSYSTEM_RAW.RATES.RATES(RATEDATE, CURRENCYCODE, RATE) VALUES ('" + \
              date_str + "','" + k + "'," + str(rates_dict.get(k)) + ")"
        print(sql)
    # snow_execute(cur, "SELECT COUNT(*) as cnt FROM DB_DEV_EVENTSYSTEM_RAW.CLOUD_OSP_2.CLIENT")
    # for (cnt) in cur:
    #    print('{0}'.format(cnt))
    cur.close()


def snow_execute(cursor, sql):
    cursor.execute(sql)


cur = snow_connect()
snow_execute(cur, "SELECT COUNT(*) as cnt FROM DB_DEV_EVENTSYSTEM_RAW.CLOUD_OSP_2.CLIENT")
for (cnt) in cur:
    print('{0}'.format(cnt))
cur.close()

