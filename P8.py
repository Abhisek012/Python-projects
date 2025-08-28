import string
import random
import getpass

def check_pass_strenght (password):
    issues = []
    if len(password) <8:
        issues.append("Too short (minimuum 8 characters)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing a special character ")
    return issues
   

def generate_strong_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation

    
    return "".join( random.choice(chars) for _ in range (length))

password = getpass.getpass("Enter a password: ")
error1 = check_pass_strenght(password)

if not error1:
    print("Strong password! you are good to go.")
else: 
    print("You got weak password!")
    for issue in error1:
        print(f"-{error1}")

while True:
    sug = input("Do you want us to suggsest you a good password (y/n): ")
    if sug.lower() == "y":
        suggestion = generate_strong_password()
        print("\nSuggesting you a strong password: ")
        print(suggestion)
        print("Thank you for the trust you've shown in us.")
        break
    else:
        break


