def calculate_discount(price, discount_percent):
    final_price = price - (price * discount_percent / 100)
    return final_price

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query
