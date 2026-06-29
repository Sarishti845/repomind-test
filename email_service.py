def send_email(user_email, subject, body):
    if not user_email:
        return False
    message = subject + body
    print("Sending to: " + user_email)
    return True

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query
