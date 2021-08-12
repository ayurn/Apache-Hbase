IMPORTING LIVE STOCK DATA INTO HBASE
Writing a python hbase program to get live data from api and then saving it to hbase table.
Step 1) import all libraries and establishing connection with hbase

Step 2) creating a table where we want to save that data
Here we are creating a table called ‘stock_live_data’ and it has 5 column families for each data we are going to get from api.

Step 3) Importing data into hbase table which we have created
We are getting our data from alphavantage website and i have provided my api key in .env file. 
So here our first row will be our unique key because it is going to be time and time is important and unique in stock data

Step 4) scanning the table we have just saved.

And now run this python program and our data will be saved in that hbase table.
python3 stock_data.py
