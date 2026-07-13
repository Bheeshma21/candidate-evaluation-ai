from parsers.resume_parser import ResumeParser

text = ResumeParser.extract_text(
    r"C:\Users\Bheeshma\Downloads\Bheeshma_Data_Scientist_2025.pdf"
)

print("=" * 50)
print("RESUME TEXT EXTRACTED SUCCESSFULLY")
print("=" * 50)

print(text[:2000])