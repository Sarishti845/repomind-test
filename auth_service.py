def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def reset_password(email):
    if email == "":
        return None
    send_email(email)
    return True