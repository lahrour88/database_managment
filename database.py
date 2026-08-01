import sqlite3

class database():
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                password TEXT NOT NULL
                )""")
            self.connection.commit()
    #        self.cursor.close()
            return "Table created successfully"
        except Exception as e:
            print(f"Error creating table: {e}")
        
    def insert_user(self, user):
        try :
            self.cursor.execute(""" INSERT INTO users(name , email , phone , password)VALUES(?,?,?,?)""",(user.name ,user.email ,user.phone ,user.password,))
            self.connection.commit()

            return "User inserted successfully"
        except Exception as e:
            print(f"Error inserting user: {e}")

    def update_user(self ,query ,id):
        """ enter the query in the form of query="name = 'new_name' , email = 'new_email' , phone = 'new_phone' , password = 'new_password'" """
        try :
            set_clause = ", ".join([f"{key} = ?" for key in args])
            self.cursor.execute(f"""
            UPDATE users SET {set_clause} WHERE id = ?
            """ , (id,))
            self.connection.commit()
            return "User updated successfully"
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete_user(self , id):
        try :
            self.cursor.execute(f"""
            DELETE FROM users WHERE id = ?
            """, (id,))
            self.connection.commit()
            return "User deleted successfully"
        except Exception as e:
            print(f"Error deleting user: {e}")

    def select_user(self  ,colomn ,condition ):
        try :
            if condition :
                query=f"WHERE {condition} "
            else :
                query=""
            if colomn == '*' :
                print(f"SELECT {colomn} FROM users {query}")
                data = self.cursor.execute(f"SELECT {colomn} FROM users {query}")
            else :
                data =self.cursor.execute(f"SELECT {colomn} FROM users {query}")
            self.connection.commit()
            return data.fetchall()
        
        except Exception as e:
            print(f"Error selecting user: {e}")