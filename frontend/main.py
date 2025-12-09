import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)          
print("Working directory set to:", os.getcwd())

from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Import screens
from scripts.login_screen import LoginScreen
from scripts.loading_screen import LoadingScreen

class LuminaScreenManager(ScreenManager):
    pass

class LuminaApp(MDApp):
    # Main application class
    # ------- GLOBAL Assets & Configuration -------
    loading_image = "assets/loading/loading_image.jpg"
    loading_animation = "assets/loading/loading_animation.json"

    Name = "Lumina"
    version = "1.0.0"

    def build(self):
        #self.theme_cls.primary_palette = "Indigo"
        #self.theme_cls.theme_style = "Light"

        sm = LuminaScreenManager()

        self.loading_kivy_path = "screens/loading.kv"
        try:
            if os.path.exists(self.loading_kivy_path):
                Builder.load_file(self.loading_kivy_path)
                print("Successfully loaded loading.kv")
            else:
                print(f"loading.kv does not exist: {self.loading_kivy_path}")
        except Exception as e:
            print("Error loading \'loading.kv\': {e}")

        # Add loading screen first, then others
        sm.add_widget(LoadingScreen(name="loading"))
        sm.add_widget(LoginScreen(name="login"))

        sm.current = "loading"

        return sm  
    
if __name__ == "__main__":
    LuminaApp().run()