from os import curdir
import sqlite3

def connect():
    con = sqlite3.connect("flask-sql-snacks.db")
    return con
def close(con,cur):
    cur.close()
    con.close()

def create_table():
    con = connect()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS snacks(\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    name TEXT,\
                    kind TEXT);")
    close(con,cur)

def get_all_snacks():
    con = connect()
    cur=con.cursor()
    cur.execute('SELECT * FROM snacks')
    snacks = cur.fetchall()
    close(con,cur)
    return snacks

def create_snack(name,kind):
    con = connect()
    cur = con.cursor()
    print(name,kind)
    cur.execute("INSERT INTO snacks (name,kind) VALUES ('{}','{}');".format(name,kind))
    con.commit()
    close(con,cur)

def show_snack_by_id(id):
    con=connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM snacks where id={}".format(id))
    snack = cur.fetchall()
    close(con,cur)
    return snack

def delete_snack_by_id(id):
    con=connect()
    cur = con.cursor()
    cur.execute("DELETE FROM snacks WHERE id={}".format(id))
    con.commit()
    close(con,cur)

def update_snack_by_id(name,kind,id):
    con = connect()
    cur=con.cursor()
    cur.execute("UPDATE snacks SET name='{}', kind='{}' WHERE id={}".format(name,kind,id))
    con.commit()
    close(con,cur)