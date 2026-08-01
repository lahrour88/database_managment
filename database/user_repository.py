import sys ,os

import models.user
from database.database import Database
db = Database(input("Enter database name: "))

def create_table():
    try :
        table_name=input("Enter table name: ")
        return db.create_table(table_name=table_name)
    except Exception as e :
        return f"Error creating table: {str(e)}"

def add_users():
    try :
        print("Add User Functionality")
        table_name =input("Enter table name: ")
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone=input("Enter phone: ")
        password=input("Enter password: ")
        user = models.user.User(table_name= table_name ,name=name ,email=email ,phone=phone ,password=password)
        return db.insert_user(User=user)
    except Exception as e :
        return f"Error adding user: {str(e)}"

def show_users():
    try :
        print("Show Users Functionality")
        table_name = input("Enter table name: ")
        coloms = input("Enter columns to select (comma-separated) or '*' for all: ")
        query = input("Enter query (e.g., WHERE id=1) or leave blank for no query: ")
        return db.select_user(table_name=table_name, coloms=coloms, condition=query)
    except Exception as e:
        return f"Error showing users: {str(e)}"

def delete_users():
    try:
        print("Delete User Functionality")
        table_name = input("Enter table name: ")
        condition = input("Enter condition for deletion (e.g., WHERE id=1): ")
        return db.delete_user(table_name=table_name, condition=condition)
    except Exception as e:
        return f"Error deleting user: {str(e)}"

def update_users():
    try :
        table_name = input("Enter table name: ")
        print("if you want to update comlmns you can enter new for colomn else leave it blank !")
        new_name = input("Enter new name (leave blank to skip): ")
        new_email = input("Enter new email (leave blank to skip): ")
        new_phone = input("Enter new phone (leave blank to skip): ")
        new_password = input("Enter new password (leave blank to skip): ")
        condition = input("Enter condition for update (e.g., WHERE id=1): ")
        return db.update_user(table_name=table_name, query=condition, name=new_name if new_name else None, email=new_email if new_email else None, phone=new_phone if new_phone else None, password=new_password if new_password else None)
    except Exception as e :
        return f"Error updating user: {str(e)}"

def login():
    try :
        table_name = input("Enter table name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        result = db.select_user(table_name=table_name, coloms="name ,email, password", condition=f"WHERE email='{email}' AND password='{password}'", search="search")
        message =f" hello {result[0][0]} your are logged in " if result else "Invalid email or password"
        return message
    except Exception as e :
        return f"Error searching user: {str(e)}"