import psycopg2

dbname = "qos"
user = ""
password = ""
host = "localhost"
port = "8886"

conn = psycopg2.connect(host=host, database=dbname, user=user, password=password, port=port)

cursor = conn.cursor()
cursor.execute("""SELECT * FROM malerttype ORDER BY id DESC LIMIT 100""")
rows = cursor.fetchall()

for row in rows:
    tt = row[4].split('.')
    if 'RCA' in tt:
        print(row)

cursor.close()
