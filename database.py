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
                            
                            DELETE FROM users
                            WHERE id <> 0;
                            
                        """)

        except AttributeError:
            print("Faça a conexão")

    def already_exists(self, user, password, email=''):
        try:
            cursor = self.connection.cursor()
            if email:
                cursor.execute("""
                    SELECT COUNT(*) FROM users WHERE user=? OR email=?
                """, (user, email))
            else:
                cursor.execute("""
                    SELECT COUNT(*) FROM users WHERE user=? OR email=? OR password=?
                """, (user, email, password))
            result = cursor.fetchone()
            return result[0] > 0
        except sqlite3.Error as error:
            print("Error while checking user exists: ", error)
            return False

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
            print(email)




if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.alter_table_users()
    db.close_connection()
