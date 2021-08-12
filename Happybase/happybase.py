'''
@Author: Ayur Ninawe
@Date: 2021-08-07
@Last Modified by: Ayur Ninawe
@Last Modified time: 17:00:47 2021-08-07
@Title : Program to import data from given file to HBase table with happybase
'''

import happybase as hb
from logger import logger
import csv
# Start thrift server first: hbase-daemon.sh start thrift


def connect_to_hbase():
    """
    Description:
        This function is used for creating connection with hbase
     Return:
        It return a conn 
    """
    try:
        conn = hb.Connection()
        conn.open()
        return conn
    except Exception as e:
        logger.error(e)

def creating_table():
    """
    Description:
        This function is used for creating hbase table
    """
    try:
        connection = connect_to_hbase()
        connection.create_table('wordcount',{'cf1': dict(max_versions=1),'cf2': dict(max_versions=1)})
        logger.info("table created successfully")
       
    except Exception as e: 
        logger.error(e)
        connection.close()

def put_csv_data_into_hbase():
    """
    Description:
        This function is used for putting csv data into hbase table
    """
    try:
        connection = connect_to_hbase()
        table = connection.table('wordcount')
        input_file = csv.DictReader(open("/home/ayur/HadoopProgram/Hbase/Happybase/wordcount_op"))
        for row in input_file:
            table.put(row['id'],
        {'cf1:String': row['word'],
         'cf2:Count': row['count']})       
    except Exception as e: 
        logger.error(e)
        connection.close()
        
def display_table_data():
    """
    Description:
        This function is used for displaying data from hbase table.
    """
    try:
        connection = connect_to_hbase()
        table = connection.table('wordcount')
        for key,data in table.scan():
            id = key.decode('utf-8')
            for value1,value2 in data.items():
                cf1 = value1.decode('utf-8')
                cf2 = value2.decode('utf-8')
                print(id,cf1,cf2) 

    except Exception as e:
        logger.error(e)


creating_table()
put_csv_data_into_hbase()
display_table_data()