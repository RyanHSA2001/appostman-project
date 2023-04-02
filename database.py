import sqlite3


class DataBase():
    def __init__(self, name="system.db") -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                CREATE TABLE IF NOT EXISTS users(
                
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                    );
                    
            """)

        except AttributeError:
            print("Faça a conexão")

    def alter_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                            
                            DROP TABLE users;
                            

                        """)

        except AttributeError:
            print("Faça a conexão")

    def auth(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM users;
                
            """)

            for line in cursor.fetchall():
                if line[1].upper() == user.upper() and line[2] == password:
                    return True
                else:
                    continue
            return False
        except:
            ...

    def insert_user(self, user, email, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                    INSERT INTO users(user, email, password) VALUES(?, ?, ?);

            """, (user, email, password))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")
        except sqlite3.IntegrityError:
            return "already_exists"


if __name__ == "__main__":
    db = DataBase()
    db.connect()
    # db.create_table_users()
    db.close_connection()
