import sounddevice as sd
import soundfile as sf

from shared.live_state import live_data


class MicrophoneRecorder:

    def record(
        self,
        filename="recordings/interview.wav",
        duration=10,
        samplerate=16000
    ):

        live_data["status"] = "🎤 Listening..."

        print("=" * 50)
        print("🎤 Recording started...")
        print(f"Using microphone device: {sd.default.device}")
        print("=" * 50)

        # Record from the working microphone (device 1)
        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32",
            device=1
        )

        sd.wait()

        # Debug information
        print(f"Max amplitude : {audio.max()}")
        print(f"Min amplitude : {audio.min()}")
        print(f"Mean amplitude: {audio.mean()}")

        sf.write(
            filename,
            audio,
            samplerate
        )

        live_data["status"] = "🧠 Processing..."

        print(f"Audio saved to: {filename}")
        print("=" * 50)

        return filename