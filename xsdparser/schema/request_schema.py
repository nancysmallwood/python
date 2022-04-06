from pyspark.shell import spark, sc
from pyspark.sql.types import StructType, StringType, LongType, DoubleType, MapType, ArrayType, StructField


def define_schema():
    data = '{"login": {"trusted_id": "******","user_name": "Nancy"},' \
           '"application_data": {"sender": "Nancy","response_time_ms": 45,' \
           '"application_properties": {' \
           '"application_properties": [{"application_property": "propxyz","key": "specialKey"}]}'

    payload_schema = StructType([
        StructField("login",
                    StructType([
                        StructField('trusted_id', StringType(), True),
                        StructField('user_name', StringType(), True)
                    ]), True),
        StructField("application_data",
                    StructType([
                        StructField('sender', StringType(), True),
                        StructField('response_time_ms', LongType(), True),
                        StructField('application_properties',
                                    StructType([
                                        StructField('application_properties', ArrayType(
                                            StructType([
                                                StructField('application_property', StringType(), True),
                                                StructField('key', StringType(), True)
                                            ]), True), True),
                                        True]), True),
                        True]), True
                    )
    ])
    # df = spark.createDataFrame(data=data, schema=payload_schema)
    df = spark.read.schema(payload_schema).json(sc.parallelize([data]))
    df.printSchema()
    df.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    define_schema()
