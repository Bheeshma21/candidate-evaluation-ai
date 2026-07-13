import smtplib
import os

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


class EmailService:

    @staticmethod
    def send_interview_email(
        to_email: str,
        candidate_name: str,
        interview_date: str,
        interview_time: str,
        interviewer: str,
        meeting_link: str
    ):

        email = EmailMessage()

        email["Subject"] = "Interview Invitation"

        email["From"] = os.getenv("EMAIL_ADDRESS")

        email["To"] = to_email

        email.set_content(
f"""
Hello {candidate_name},

Congratulations!

Your interview has been scheduled.

Date : {interview_date}
Time : {interview_time}

Interviewer:
{interviewer}

Meeting Link:
{meeting_link}

Best of luck!

HR Team
"""
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

            smtp.starttls()

            smtp.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )

            smtp.send_message(email)
    @staticmethod
    def send_shortlisted_email(
        to_email: str,
        candidate_name: str,
        score: float
    ):

        email = EmailMessage()

        email["Subject"] = "Congratulations! You Have Been Shortlisted"

        email["From"] = os.getenv("EMAIL_ADDRESS")
        email["To"] = to_email

        email.set_content(
f"""
Hello {candidate_name},

Congratulations!

Your resume has been successfully evaluated by our AI Recruitment System.

Overall Match Score: {score}%

You have been shortlisted for the next stage of the hiring process.

Our recruitment team will review your profile and send you an interview invitation shortly if everything is confirmed.

Thank you for your interest.

Best Regards,
HR Team
"""
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

            smtp.starttls()

            smtp.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )

            smtp.send_message(email)