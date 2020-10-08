import sqlite3

data = []
conn = sqlite3.connect('crawler.db')

c = conn.cursor()

def execute_tables():
    c.execute('''CREATE TABLE directories
            (inode_number, hard_link_count, user_id, group_id, \
                size, mode, access_time, modified_time, full_pathname, \
                    file_extension, inode_mcd, full_path_name, file_extension, \
                file_size, soft_or_hard_link, user_or_group_id, \
                    , mac)''')
    
    c.execute('''CREATE TABLE file
            (inode_number, inode_mcd, full_path_name, file_extension, \
                file_size, soft_or_hard_link, user_or_group_id, \
                    hard_link_count, mac)''')

def insert_data(data):
    c.executemany("INSERT INTO directories VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

execute_tables()
insert_data(data)
conn.commit()
conn.close()
