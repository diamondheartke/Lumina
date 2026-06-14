"""
Loading screen helper.
Loads KV files in a background thread to avoid blocking the UI, then
switches to the 'login' screen on the main thread when done.

"""

<<<<<<< HEAD

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread

=======
from tkinter import Image
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.uix.floatlayout import FloatLayout
>>>>>>> d345f3b848890f7f6c947c400d40f26792b8fcc8
import threading
import os


<<<<<<< HEAD
main_kv_files = [
    "frontend/screens/login.kv",
    "frontend/screens/signup.kv",
    "frontend/screens/home.kv"   
]

secondary_kv_files = [
    "frontend/screens/lesson.kv",
    "frontend/screens/quiz.kv",
    "frontend/screens/tasks.kv",
    "frontend/screens/profile.kv",
    "frontend/screens/tutor.kv",
    "frontend/screens/lesson_progress.kv",
    "frontend/screens/mini_quest.kv",
    "frontend/screens/timetable.kv"
]

class LoadingScreen(MDScreen):
    """Screen that loads KV files in background, then navigates to login."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dot_state = 0

    def on_enter(self):
        self.dot_state = 0
        self.is_loaded = False
        self.ids.loading_slider.value = 0
        Clock.schedule_interval(self.animate_dots, 0.25)

        self.image_path = "frontend/assets/loading/loading_image.jpg"
        print("Image path exists:", os.path.exists(self.image_path))
        print("LoadingScreen entered")

        thread = threading.Thread(target=self.load_kv, daemon=True)
        thread.start()

    def animate_dots(self, dt):
        # Update loading dots
        self.dot_state = (self.dot_state + 1) % 4
        self.ids.loading_text.text = "Loading" + "." * self.dot_state

        slider = self.ids.loading_slider
        if slider.value < slider.max:
            slider.value = min(slider.max, slider.value + 8)

        if self.is_loaded and slider.value >= slider.max:
            Clock.unschedule(self.animate_dots)
            self._go_to_login(0)

    def load_kv(self):
        for kv in main_kv_files:
            try:
                path = kv
=======
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
>>>>>>> d345f3b848890f7f6c947c400d40f26792b8fcc8
                if os.path.exists(path):
                    Builder.load_file(kv)
                    print(f"Loaded {kv} successfully.")
                else:
                    print(f"KV file not found: {path}")
            except Exception as e:
                print(f"Error loading {kv}: {e}")

<<<<<<< HEAD
        self.is_loaded = True
=======
        # switch to login on the main thread
        Clock.schedule_once(self._go_to_login, 5)
>>>>>>> d345f3b848890f7f6c947c400d40f26792b8fcc8

    @mainthread
    def _go_to_login(self, dt):
        if self.manager:
            try:
                self.manager.current = "login"
            except Exception as e:
                print(f"Failed to change screen: {e}")