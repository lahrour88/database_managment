class User():
    def __init__(self ,name , email , phone , password):
        self.table_name = "users"
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
