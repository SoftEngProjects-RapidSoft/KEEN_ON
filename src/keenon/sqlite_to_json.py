import sqlite3
import sys
import os

def outputJSONObject(key, val, last):
	if val is None:
		val = ''
	obj = ''
	obj += '\t\t"' + str(key).lower() + '" : '
	obj += '"' + str(val) + '"'
	if last != True:
		obj+=','
	obj+='\n'
	return obj

path = os.getcwd()
new_directory_path = f"{path}/db_json"

try:
    os.mkdir(new_directory_path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

db = f"db.sqlite3"
con = sqlite3.connect(db)
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = [item[0] for item in cur.fetchall()]

for table in tables:
    cur = con.cursor()
    cur.execute("select * from " + table)

    col_names = [cn[0] for cn in cur.description]
    completeName = os.path.join(new_directory_path, f"{table}.json")

    with open(completeName, "w") as f:
        f.write("[\n")

        items = cur.fetchall()
        for i, item in enumerate(items):
            if item == None:
                break
            json = '\t{\n'
            for j, col in enumerate(col_names):
                last = j == (len(col_names)-1)
                json += outputJSONObject(col, item[col], last)

            if i != (len(items)-1):
            #if i < 10000:
                json += '\t},\n'
            else:
                json += '\t}\n'
            f.write(json)
        f.write("]")
    cur.close()