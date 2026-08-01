from user import user
import database
data =[{
    'name' : 'John Doe',
    'email' : 'johndoe@exemple.com ',
    'phone' : '1234567890',
    'password' : 'password123'
},{
    'name' : 'Jane Smith',
    'email' : 'janesmith@exemple.com',
    'phone' : '0987654321',
    'password' : 'password456'
},{
    'name' : 'Alice Johnson',
    'email' : 'alicejohnson@exemple.com',
    'phone' : '1122334455',
    'password' : 'password789'
}]
db=database.database()

#create table
print(db.create_table())
print("-"*20)
#add user 
for users in data :
    print(db.insert_user(user( name=users['name'], email=users['email'], phone=users['phone'], password=users['password'])))
    print("-"*20)
#update user
print(db.update_user(query = "name='lahrour',password='updatedpassword'", id = 1))
print("-"*20)
#slect user an users
print(db.select_user(colomn = "*", condition = "id =1"))
print("-"*20)
print(db.select_user(colomn = "*", condition = "id>0")) #or condition = ""
print("-"*20)
print(db.delete_user(id = 2))