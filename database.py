import sqlite3
def creat_db():
    con=sqlite3.connect(database=r'sms.db')
    cur=con.cursor()
#employee_table
    cur.execute('create table if not exists employee(eid integer primary key autoincrement,name text,email text,gender text,contact text,dob text,doj text,password text,utype text,salary text,address text)')
    con.commit()
#supplier_table
    cur.execute('create table if not exists supplier(invoice integer primary key autoincrement,name text,contact text)')
    con.commit()
#category_table
    cur.execute('create table if not exists category(cid integer primary key autoincrement,name text)')
    con.commit()
#product_table
    cur.execute('create table if not exists product(pid integer primary key autoincrement,supplier text,category text,name text,price text,qty text,status text)')
    con.commit()
creat_db()