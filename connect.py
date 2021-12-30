import sqlite3

def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXIST  OYO_HOTEL(NAME TEXT , ADDRESS TEXT ,PRICE INT ,AMENITY TEXT ,RATING TEXT)")
    conn.close()

def insert(dbname,values):
    conn=sqlite3.connect(dbname)
    conn.execute("INSERT INTO  OYO_HOTEL(NAME ,ADDRESS ,PRICE ,AMENITY ,RATING) VALUES (?,?,?,?,?)",values)
    conn.commit()
    conn.close()


def get_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM  OYO_HOTEL")

    table=cur.fetchall()


    for record in table:
        print(record)
    conn.close()    
