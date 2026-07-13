import threading
import pyttsx3

from shared.live_state import live_data


class TextToSpeech:

    def __init__(self):

        # Create ONE engine only
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

        # Prevent two speak() calls at the same time
        self.lock = threading.Lock()

    def speak(self, text: str):

        live_data["question"] = text

        with self.lock:

            self.engine.say(text)
            self.engine.runAndWait()