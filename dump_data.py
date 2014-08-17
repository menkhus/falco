#!/usr/bin/env python
# X phase zero build a data structure that represents the entire vfeed database
# phase one put this database into json form
# phase two put this database intp neo4j graph database
# Mark Menkhus August 9, 2014

database='vfeed.db'
vfeed = {}
import sqlite3
from sys import getsizeof as sizeof
con = sqlite3.connect(database)
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
#create a dictionary to store all the table data in
for item in tables:
    vfeed[item[0]] = []
print "data in the %s database is as follows:"%(database,)
size = 0
for each in tables:
    #print each[0]
    cursor.execute("select * from " + each[0])
    # this prints all the data, at this point, you can use
    # cursor.fetchall() to pull the
    # data and load it by table name into a json data structure.
    try:
        table_size = 0
        table = cursor.fetchone()
        desc = cursor.description
        rownames = []
        for row in desc:
            rownames.append(row[0])
        #print rownames
        #print table
        table_size += sizeof(table)
        table = dict(zip(rownames,table))
        #print table
        vfeed[each[0]].append(table)
        #print vfeed
        while table is not None:
            try:
                table=cursor.fetchone()
                table_size += sizeof(table)
                table = dict(zip(rownames,table))
                vfeed[each[0]].append(table)
            except Exception as e:
                #print "\texception INNER LOOP : could not decode an item from %s table"%(each[0])
                pass
    except Exception as e:
        print "\texception: could not decode an item from %s table"%(each[0])
        pass
    print "table %s: is %s kilobytes"%(each[0],table_size/1000.0)
    size += table_size
cursor.close()
print "total data is \t\t\t%s megabytes"%(size/1000000.0,)
# you have to walk the whole vfeed dictionary to measure the size
vfeed_size = 0
for table in vfeed:
    for item in vfeed[table]:
        vfeed_size += sizeof(item)
        #print table,item
print "total size of vfeed structure is \t\t\t%s megabytes"%(vfeed_size/1000000.0,)

print vfeed.keys()
for each in vfeed.keys():
    for e in vfeed[each]:
        print each,e