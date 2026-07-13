import os
import whisper

from shared.live_state import live_data


class SpeechToText:

    def __init__(self):

        ffmpeg_path = r"C:\Users\Bheeshma\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin"

        os.environ["PATH"] = (
            ffmpeg_path
            + os.pathsep
            + os.environ["PATH"]
        )

        self.model = whisper.load_model("base")

    def transcribe(self, audio_path: str):

        result = self.model.transcribe(audio_path)

        text = result["text"].strip()

        live_data["answer"] = text
        live_data["status"] = "✅ Answer received"

        return text