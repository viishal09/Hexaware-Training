class PasswordValidator:
    @staticmethod
    def validate_password(password):
        if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
            print("Password is valid.")
        else:
            print("Invalid password. Please follow the password rules.")