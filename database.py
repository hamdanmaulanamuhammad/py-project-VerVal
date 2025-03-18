""" Modul untuk mengelola koneksi database MySQL """

import mysql.connector

def get_db_connection():
    """ Mengembalikan koneksi ke database MySQL """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventaris"
    )
    return conn
