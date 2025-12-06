from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class LuminaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"

        return MDLabel(
            text="Welcome to Lumina!",
            halign="center",
            valign="center",
            font_style="H3",
            theme_text_color='Primary'
        )
    
if __name__ == "__main__":
    LuminaApp().run()