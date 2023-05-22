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

    def create_table_recipients(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS recipients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(20) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE
                )
                """)

        except AttributeError:
            print("Faça a conexão")

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

    def update_password(self, user, new_password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE users SET password = ? WHERE user = ?
            """, (new_password, user))

            self.connection.commit()

            cursor.close()

            return True
        except sqlite3.Error as error:
            print("Error while updating password: ", error)
            return False

    def already_exists(self, user, password, email=''):
        try:
            cursor = self.connection.cursor()
            if email:
                cursor.execute("""
                    SELECT COUNT(*) FROM users WHERE user=? OR email=?
                """, (user, email))
            else:
                cursor.execute("""
                    SELECT COUNT(*) FROM users WHERE user=? AND password=?
                """, (user, password))
            result = cursor.fetchone()
            return result[0] > 0
        except sqlite3.Error as error:
            print("Error while checking user exists: ", error)
            return False

    def search_email(self, email):
        try:
            cursor = self.connection.cursor()

            cursor.execute("""
                        SELECT * FROM users WHERE email=?
                    """, (email,))

            result = cursor.fetchone()
            cursor.close()
            return result

        except sqlite3.Error as error:
            print("Error while checking email exists: ", error)
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

    def insert_recipient(self, name, email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT OR REPLACE INTO recipients(name, email) VALUES(?, ?)
                
            """, (name, email))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")

    def show_recipients(self):
        try:
            cursor = self.connection.cursor()

            cursor.execute("""
            
                    SELECT name, email FROM recipients
            
                """)

            result = cursor.fetchall()
            cursor.close()
            return result

        except sqlite3.Error as error:
            print("Error while checking recipients: ", error)
            return False

if __name__ == "__main__":
    db = DataBase()
    db.connect()

    result = db.show_recipients()

    print(result)

    db.close_connection()
