#frontend/scripts/LoginScreen.py

from kivymd.uix.screen import MDScreen
import re

class LoginScreen(MDScreen):
    def on_enter(self):
        print("Login screen entered")

    def try_login(self):    
        print("Login attempt initiated")
        self.manager.current = "home"

    def switch_to_signup(self):
        self.manager.current = "signup"

    def validate_email(self, email):
        pattern = r''
        is_valid = re.match(pattern, email) is not None
        print(f"Email validation for '{email}': {is_valid}")
        return is_valid
    
    def validate_password(self, password):
        length = len(password)
        character_types = sum(bool(re.search(pattern, password)) for pattern in [r'[A-Z]', r'[a-z]', r'[0-9]', r'[\W_]'])
        is_valid = length >= 6 and character_types >= 2
        print(f"Password validation: {is_valid}")
        return {
            "is_valid": is_valid,
            "length": length,
            "character_types": character_types
        }
    