import sqlite3
import os
from sqlite3 import Error


current_dir = os.getcwd()


def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_table):
    try:
        c = conn.cursor()
        c.execute(sql_table)
    except Error as e:
        print(e)


def main():
    sql_create_file_table = """CREATE TABLE IF NOT EXISTS file
    (
        id integer AUTO_INCREMENT PRIMARY KEY,
        inode_number integer NOT NULL,
        hardlink_count integer NOT NULL,
        user_id integer NOT NULL,
        group_id integer NOT NULL,
        size integer NOT NULL,
        mode integer NOT NULL,
        access_time integer NOT NULL,
        modified_time integer NOT NULL,
        full_pathname text NOT NULL,
        file_extension text,
        file_size text NOT NULL,
        soft_or_hardlink text
    );"""

    conn = create_connection('crawler.db')

    if conn is not None:
        print(conn.cursor())
        create_table(conn, sql_create_file_table)
    else:
        print("Error! cannot create the database connection")


if __name__ == '__main__':
    main()
