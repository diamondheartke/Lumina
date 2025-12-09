import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)          
print("Working directory set to:", os.getcwd())

from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager


# Import screens
from scripts.login_screen import LoginScreen
from scripts.loading_screen import LoadingScreen

class LuminaScreenManager(ScreenManager):
    pass

class LuminaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"

        sm = LuminaScreenManager()

        # Add animation screen first, then others
        sm.add_widget(LoadingScreen(name="loading"))
        sm.add_widget(LoginScreen(name="login"))

        sm.current = "loading"

        return sm  
    
if __name__ == "__main__":
    LuminaApp().run()