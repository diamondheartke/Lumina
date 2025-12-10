"""
Loading screen helper.
Loads KV files in a background thread to avoid blocking the UI, then
switches to the 'login' screen on the main thread when done.

"""

from tkinter import Image
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.uix.floatlayout import FloatLayout
import threading
import os


kv_files = [
    "screens/login.kv",
    "screens/signup.kv",
    "screens/home.kv",
    "screens/lesson.kv",
    "screens/quiz.kv",
    "screens/timetable.kv"
]


class LoadingScreen(MDScreen):
    """Screen that loads KV files in background, then navigates to login."""

    def on_enter(self):
        #self.relative_image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "loading", "loading_image.jpg")
        #self.ids.loading_image.source = "assets/loading/loading_image.jpg"
        self.image_path = "assets/loading/loading_image.jpg"
        print("Image path exists:", os.path.exists(self.image_path))
        print("LoadingScreen entered")
        self.load_kv()
        
    def load_kv(self):
        for kv in kv_files:
            try:
                path = os.path.join(os.path.dirname(__file__), "..", kv)
                if os.path.exists(path):
                    Builder.load_file(kv)
                    print(f"Loaded {kv} successfully.")
                else:
                    print(f"KV file not found: {path}")
            except Exception as e:
                print(f"Error loading {kv}: {e}")

        # switch to login on the main thread
        Clock.schedule_once(self._go_to_login, 5)

    @mainthread
    def _go_to_login(self, dt):
        if self.manager:
            try:
                self.manager.current = "login"
            except Exception as e:
                print(f"Failed to change screen: {e}")