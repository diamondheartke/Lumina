#frontend/scripts/LoginScreen.py

from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def on_enter(self):
        print("Login screen entered")

    def switch_to_signup(self):
        self.manager.current = "signup"

    def toggle_password(self):
        self.ids.password_field.password = not self.ids.password_field.password
        self.ids.password_field.icon_right = "eye-outline" if self.ids.password_field.password else "eye-off-outline"