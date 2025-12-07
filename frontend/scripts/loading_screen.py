"""
Loading screen helper.
Loads KV files in a background thread to avoid blocking the UI, then
switches to the 'login' screen on the main thread when done.

"""

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
import threading


kv_files = [
    "screens/login.kv",
    "screens/loading.kv",
    "screens/lesson.kv",
    "screens/quiz.kv",
    "screens/timetable.kv",
]


class LoadingScreen(MDScreen):
    """Screen that loads KV files in background, then navigates to login."""

    def on_enter(self):
        print("LoadingScreen entered")
        threading.Thread(target=self.load_kv, daemon=True).start()

    def load_kv(self):
        for kv in kv_files:
            try:
                Builder.load_file(f"frontend/{kv}")
                print(f"Loaded {kv} successfully.")
            except Exception as e:
                print(f"Error loading {kv}: {e}")

        # switch to login on the main thread
        Clock.schedule_once(self._go_to_login, 0)

    def _go_to_login(self, dt):
        if self.manager:
            try:
                self.manager.current = "login"
            except Exception as e:
                print(f"Failed to change screen: {e}")