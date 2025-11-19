def login(email, password):
    if not isinstance(email, str) or not isinstance(password, str):
         return "Error: email and password are not strings"
    if '@' not in email:
            print('invalid')
            return "invalid email"
    if len(password) < 8:
         return "invalid password"
    if password.isdigit not in password:
        return "Not valid password"
    for i in password:
        if i.isupper in password:
            print('valid')
            return "a valid password"
        else:
            print('invalid')
            return "Not valid password"
login("email@email.email", "qwertyUiopasdfghjk1zxcvbnm")


