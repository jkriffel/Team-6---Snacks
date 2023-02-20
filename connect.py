import flask
import os
from flask import send_from_directory
import psycopg2

DB_HOST = "ec2-52-201-124-168.compute-1.amazonaws.com"
DB_NAME = "daf852u68chkv6"
DB_USER = "ymvkfvfaiyyqrb"
DB_PASS = "0bb71cbd549be10c112e262649118e7fa139c06835b6417c3f20521868c00165"


app = flask.Flask(__name__)
try:
    conn = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)
except Exception:
    print("connection failed")

def check_user_by_id(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM player WHERE id = %s;", (id,))
    if cur.fetchone():
        cur.close()
        return True
    else:
        cur.close()
        return False
    
def get_user_codename(id):
    cur = conn.cursor()

    if check_user_by_id(id):
        cur.execute("SELECT * FROM player WHERE id = %s;", (id,))
        user = cur.fetchone()
        cur.close()
        return user[3]
    else:
        cur.close
        return "no user found"
        print("user does not exist")
