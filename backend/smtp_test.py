import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

print("Email:", email)
print("Password length:", len(password))

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(email, password)
    print("✅ Login successful")
    smtp.quit()
except Exception as e:
    print("❌ Error:", e)