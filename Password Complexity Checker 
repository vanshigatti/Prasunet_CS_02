import re
def check_password_strength(password):
    length = len(password)
    score = 0
    if length < 8:
        return "Weak: Password length should be at least 8 characters."
    elif length < 12:
        score += 1
    else:
        score += 2
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        return "Weak: Password should contain both uppercase and lowercase letters."
    if re.search("[0-9]", password):
        score += 1
    else:
        return "Weak: Password should contain numbers."
    if re.search("[!@#$%^&*()_+{}:<>?]", password):
        score += 1
    else:
        return "Weak: Password should contain special characters like !@#$%^&*()_+{}:<>?"
    if score < 3:
        return "Medium: Password could be stronger."
    elif score < 5:
        return "Strong: Good password."
    else:
        return "Very Strong: Excellent choice for a password!"
password = input("Enter your password: ")
print(check_password_strength(password))