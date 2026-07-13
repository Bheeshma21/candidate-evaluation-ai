from voice.microphone import MicrophoneRecorder
from voice.speech_to_text import SpeechToText


class InterviewSession:

    def __init__(self):
        self.recorder = MicrophoneRecorder()
        self.stt = SpeechToText()

    def start(self):

        audio_file = self.recorder.record()

        text = self.stt.transcribe(audio_file)

        print("\nCandidate said:\n")

        print(text)

        return text


if __name__ == "__main__":

    InterviewSession().start()