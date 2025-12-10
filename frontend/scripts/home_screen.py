from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.animation import Animation


class HomeScreen(MDScreen):
    def on_enter(self, *args):
        print("Home screen entered")
        # Logo pulse once when entering the screen
        Clock.schedule_once(self._pulse_logo, 0.8)

    def _pulse_logo(self, dt):
        logo = self.ids.get('logo')
        if logo:
            anim = (Animation(opacity=0.45, duration=1.0, t='out_quad') +
                    Animation(opacity=1.0, duration=1.0, t='out_quad'))
            anim.repeat = False
            anim.start(logo)