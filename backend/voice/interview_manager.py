import asyncio

from voice.microphone import MicrophoneRecorder
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech

from shared.live_state import live_data
print("INTERVIEW MANAGER:", id(live_data))
from services.interview_service import InterviewService

from agents.voice_interviewer_agent import VoiceInterviewerAgent
from agents.evaluation_agent import EvaluationAgent
from agents.report_agent import ReportAgent


class InterviewManager:

    def __init__(self):
        self.interview_service = InterviewService()

        self.recorder = MicrophoneRecorder()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        self.agent = VoiceInterviewerAgent()
        self.evaluator = EvaluationAgent()
        self.report_agent = ReportAgent()

    async def start(self, job_description: str):

        history = []

        live_data["status"] = "Interview Started"
        live_data["question"] = ""
        live_data["answer"] = ""

        print("Interview Started")
        print("LIVE:", live_data)

        # Run TTS in a worker thread
        self.tts.speak("Welcome to interview.")

        for i in range(5):

            # LLM question
            question = await self.agent.ask_question(
                job_description,
                history
            )

            live_data["status"] = f"Question {i+1}/5"
            live_data["question"] = question
            print(live_data)
            live_data["answer"] = ""

            print("\n==============================")
            print(f"QUESTION {i+1}")
            print("LIVE:", live_data)
            print("==============================")

            # Speak question without blocking FastAPI
            await asyncio.to_thread(
                self.tts.speak,
                question
            )
            await asyncio.to_thread(
                self.tts.speak,
                "Welcome to interview."
            )

            live_data["status"] = "🎤 Listening..."

            # Record microphone in worker thread
            audio_file = await asyncio.to_thread(
                self.recorder.record
            )

            live_data["status"] = "🧠 Transcribing..."

            # Whisper transcription in worker thread
            answer = await asyncio.to_thread(
                self.stt.transcribe,
                audio_file
            )

            live_data["answer"] = answer
            live_data["status"] = "✅ Answer received"

            print("ANSWER:", answer)
            print("LIVE:", live_data)

            live_data["status"] = "📝 Evaluating..."

            evaluation = await self.evaluator.evaluate(
                question,
                answer
            )

            history.append(
                {
                    "question": question,
                    "answer": answer,
                    "evaluation": evaluation
                }
            )

        live_data["status"] = "📄 Generating Report..."

        report = await self.report_agent.generate(
            history
        )

        interview_id = self.interview_service.save(
            job_description,
            history,
            report
        )

        live_data["status"] = "Interview Completed"
        live_data["question"] = "Interview Completed ✅"
        live_data["answer"] = ""

        print("Interview Completed")
        print("LIVE:", live_data)

        self.tts.speak("The interview has been completed. Thank you.")

        return {
            "interview_id": interview_id,
            "history": history,
            "report": report
        }