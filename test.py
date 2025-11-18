def login(email, password):
    if email not in '@':
        return "Not a valid email"
    if len(password) != 8 and int(password, base = 0) not in password:
        return "Not valid password"
    if password is not password.capitalize:
        return "not a valid password"
    
login("email@email.com", 'password')

