'''
@Author: Ayur Ninawe
@Date: 2021-08-12
@Last Modified by: Ayur Ninawe
@Last Modified time: 18:00:47 2021-08-12
@Title : Program to import data from given file to HBase table with happybase
'''

import happybase as hb
from loggerfile import logger
import csv
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

def establish_hbase_connection():
    """
    Description:
        This function will create connection with hbase.
    """
    try:
        conn = hb.Connection()
        conn.open()
        return conn
    except Exception as e:
        logger.info(e)

def create_table():
    """
    Description:
        This function will create table in hbase with given name and column family.
    """
    try:
        connection = establish_hbase_connection()
        connection.create_table('stock_live_data',{'cf1':dict(max_versions=1),'cf2':dict(max_versions=1),'cf3':dict(max_versions=1),'cf4':dict(max_versions=1),'cf4':dict(max_versions=1),'cf5':dict(max_versions=1)})
        logger.info("Table created")
    except Exception as e:
        logger.info(f"Errorr!!{e}")
        connection.close()

def import_into_hbase():
    """
    Description:
        This function will import data from stock API in HBase table the we created.
    """
    try:
        connection=establish_hbase_connection()
        table = connection.table('stock_live_data')
        key_data = os.getenv("KEYS")
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey={}'.format(key_data)

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            next(cr)
            my_list = list(cr)
            for row in my_list:
                table.put(row[0],
                {'cf1:open': row[1],
                'cf2:high':row[2],
                'cf3:low': row[3],
                'cf4:close': row[4],
                'cf5:volume': row[5]})
    except Exception as e:
        logger.info(f"Error!!{e}")
        connection.close()

def scan_table():
    """
    Description:
        This function will scan the table in HBase and print the data.
    """
    try:
        connection = establish_hbase_connection()
        table = connection.table('stock_live_data')
        for key,data in table.scan():
            id = key.decode('utf-8')
            for value1, value2 in data.items():
                cf1 = value1.decode('utf-8')
                cf2 = value2.decode('utf-8')
                print(id,cf1,cf2)
    except Exception as e:
        logger.info(e)

establish_hbase_connection()
create_table()
import_into_hbase()
scan_table()