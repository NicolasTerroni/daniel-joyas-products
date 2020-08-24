import pymysql
import password
from tkinter import messagebox


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=password.contra,
            db="daniel-joyas"
        )

        self.cursor = self.connection.cursor()
        messagebox.showinfo("Connected","Connection established.")


def connect():
    connect = Database()


def show_help():
    messagebox.showinfo("User guide","""
    Start conecting with the database by BBDD > Connect


    -CREATE: fill all the fields (only material, large and size can be null) then click on CREATE.

    -SEARCH: fill the fields that you are looking for an click on SEARCH.

    -UPDATE: fill the ID field, click on UPDATE, fill with the new fields and accept.

    -DELETE: fill the ID field, click on DELETE and accept.

    -LIST: click on LIST to show all the registers.

    -CLEAR: click on CLEAR to clear all the fields and the table.


    BBDD > Exit to close the aplication.
    """)
