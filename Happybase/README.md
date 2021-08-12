Importing with happybase

First start all the hadoop daemons $ start-all.sh

Then start hbase $ start-hbase.sh

Start hbase thrift server $ hbase-daemon.sh start thrift

check if all daemons are running $jps

Write a python code with happybase library to establish connection with hbase

create functions for setting up connections, creating table, importing data, and to scan table

run the code

This will import file into hbase table that we created