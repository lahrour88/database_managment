from database.database import Database
from models.user import User
from models.user import User
user= User(table_name="users",name='miloud',email="miloud@mail.com",password ="miloud123@",phone="0615500436")
db = Database("database.db")
print(db.select_user("users", "*" ,condition="phone = '0615500436'"))
db.close()