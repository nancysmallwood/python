import json
import unittest

from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *
from schema.schema import login_schema


class TestStringMethods(unittest.TestCase):

    def test_login_schema(self):
        df = (
            spark.read
                .schema(login_schema)
                .json("login.json")
        )
        self.assertEqual(df.count(), 1)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

#    def setUp(self):
#       self.source = schema.osp_source_schema(["filename.txt", 7, "request_type"])

#   def tearDown(self):
#       self.source.dispose()
