import sqlite3
from unicodedata import name

from models import user
class Database():
    """
    A class to manage SQLite database operations.
    ### operations: 
    ##### create_table(table_name)
    ##### insert_user(table_name, User)
    ##### select_user(table_name, coloms, condition=None)
    ##### update_user(table_name, query, name=None, email=None, phone=None, password=None, id=None, coloms=None)
    ##### delete_user(table_name, id)
    - database_file: str - The path to the SQLite database file.
    - table_name: str - The name of the table to operate on.
    - User: object - An instance of the User class containing user data.
    - dont forget to close the connection after using the database
    """
    def __init__(self ,database_file):
        self.database_file = database_file
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def create_table(self ,table_name):
        """ Create a table in the database if it does not already exist. """
        try:
            if not table_name:
                return "Table name is required"

            # Check if table already exists
            self.cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
                (table_name,)
            )
            exists = self.cursor.fetchone()
            if exists:
                return f"Table {table_name} already exists"

            sql = f"""
                CREATE TABLE {table_name} (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                    )"""
            self.cursor.execute(sql)
            self.connection.commit()
            return f"Table {table_name} created successfully"
        except sqlite3.Error as e:
            return f"Error creating table: {e}"
        
    def insert_user(self,User):
        try :
            self.cursor.execute(f""" INSERT INTO {User.table_name}(name , email , phone , password)VALUES(?,?,?,?)""",(User.name ,User.email ,User.phone ,User.password,))
            self.connection.commit()

            return "User inserted successfully"
        except sqlite3.Error as e:
            return f"Error inserting user: {e}"
    def select_user(self ,table_name, coloms = None ,condition=None ,search=None):
        """ exemple coloms = 'name , email , age '"""
        try :
            if search == 'search' :
                query = condition
            else :
                if condition :
                    query = f"WHERE {condition}"
                else :
                    query = None

            if coloms == "*" :
                sql = f"SELECT * FROM {table_name} {query}"
            elif coloms == None or coloms =="" :
                sql = f"SELECT * FROM {table_name} {query}"
            else :
                sql = f"SELECT {coloms} FROM {table_name} {query}"
            data = self.cursor.execute(sql)
            self.connection.commit()
            return data.fetchall()
        except sqlite3.Error as e:
            return f"Error selecting user: {e} ;{sql}"

    def update_user(self ,table_name ,query, name=None , email=None , phone=None , password=None ,id=None , coloms=None):
        """ colomns updates for exemple : name = 'new_name' , email = 'new_email' , phone = 'new_phone' , password = 'new_password' """
        try :
            if name :
                if coloms :
                    coloms += f" , name = '{name}'"
                else :
                    coloms = f"name = '{name}'"
            if email :
                if coloms :
                    coloms += f" , email = '{email}'"
                else :
                    coloms = f"email = '{email}'"
            if phone :
                if coloms :
                    coloms += f" , phone = '{phone}'"
                else :
                    coloms = f"phone = '{phone}'"
            if password :
                if coloms :
                    coloms += f" , password = '{password}'"
                else :
                    coloms = f"password = '{password}'"
            if coloms is None :
                return "No columns to update"
            else :
                print(f"coloms : {coloms} \n")
                sql = f"UPDATE {table_name} SET {coloms} WHERE {query}"
                print(f"sql : {sql} \n")
                self.cursor.execute(sql)
                self.connection.commit()
                return "User updated successfully"
        except sqlite3.Error as e:
            return f"Error updating user: {e}"

    def delete_user(self ,table_name, id):
        try :
            self.cursor.execute(f"""
            DELETE FROM {table_name} WHERE id = ?
            """, (id,))
            self.connection.commit()
            return "User deleted successfully"
        except Exception as e:
            return f"Error deleting user: {e}"
        
    def close(self):
        """ Close the database connection. """
        self.connection.close()

    def drop_table(self, table_name):
        """ Drop a table from the database. """
        try:
            self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            self.connection.commit()
            return f"Table {table_name} dropped successfully"
        except sqlite3.Error as e:
            return f"Error dropping table: {e}"