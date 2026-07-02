import os

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query

def update_password(user_id, new_password):
    if new_password == "":
        return False
    query = "UPDATE users SET password = '" + new_password + "'"
    return query

def delete_user(user_id):
    query = "DELETE FROM users"
    return query

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email, password=[]):
        self.users.append({"name": name, "email": email, "password": password})
    
    def get_all(self):
        return self.users