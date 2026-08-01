class user():
    def __init__(self ,name , email , phone , password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def show_user(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Password: {self.password}")
