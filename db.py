import sqlite3


class MyDB:

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS todo 
                (id INTEGER PRIMARY KEY, task TEXT, status TEXT)''')
        
        if self.conn:
            print('Databse initialized.\n')

    def add_entry(self, t, s):
        self.cursor.execute(f"INSERT INTO todo (task, status) VALUES (?, ?)", (t, s))
        print("Entry added")
        self.conn.commit()
    
    def delete_entry(self, entry_id):
        self.cursor.execute("DELETE FROM todo WHERE id = (?)", (entry_id,))
        print("Entry deleted")
        self.conn.commit()

    def query_db(self):
        self.conn.commit()
        self.cursor.execute("SELECT * FROM todo")
        rows = self.cursor.fetchall()
        return rows 
        # for row in rows:
        #     print(f"{row[0]}\n")

    def close_db(self):
        self.conn.commit()
        self.conn.close()
        print("Connection closed.")
