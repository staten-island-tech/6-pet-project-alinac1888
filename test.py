def login(email, password):
    if not isinstance(email, str) or not isinstance(password, str):
         return "Error: email and password are not strings"
    
    if '@' not in email:
            return "invalid email"
    
    if len(password) < 8:
            return "invalid password"
    
    if not any(num.isdigit() for num in password):
            return "Not valid password"
    
    if not any(ch.isupper() for ch in password):
            return "invalid password"
    return{'email': email, 'password': password}
print(login("email@email.email", "Uquwuuqiwdszidjkjkdkkdajdk11"))


