import sqlite3
import os


current_dir = os.getcwd()
db_path = os.path.join(current_dir, "crawler.db")

class DB_Conn:

    def __init__(self):
        pass

    def create_connection(database):
        try:
            conn = sqlite3.connect('crawler.db')
            return conn
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        return conn


class Creations(DB_Conn):
    
    def execute_tables(conn, create_sql_table):
        try:
            c = conn.cursor()
            c.execute(create_sql_table)
        except Error as e:
            print(e)

    def create_tables():
        create_file_sql_table = """CREATE TABLE IF NOT EXISTS file
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

        conn = create_connection(db_path)

        if conn is not None:
            execute_tables(conn, create_file_sql_table)
        else:
            print("Error with database creation")


    def execute_file_entry(conn, table):
        query = 'INSERT INTO file VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
        cur = conn.cursor()
        cur.execute(sql, table)
        conn.commit()
        return cur.lastrowid


    def create_file_entry(query):
        conn = create_connection(db_path)

        with conn:
            entry = query
            file_id = execute_file_entry(conn, entry)
