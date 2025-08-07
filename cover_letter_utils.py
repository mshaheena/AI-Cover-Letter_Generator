import pdfplumber
from transformers import pipeline

# Use flan-t5 or distilbart for generation
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def extract_text_from_resume(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def generate_cover_letter(resume_text, job_description):
    prompt = (
        f"Write a professional cover letter for the following job:\n\n"
        f"Job Description: {job_description}\n\n"
        f"Candidate Resume: {resume_text}\n\n"
        f"Cover Letter:"
    )
    result = generator(prompt, max_length=400, do_sample=True)
    return result[0]['generated_text']

def export_cover_letter_to_pdf(text, filename="cover_letter.pdf"):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
    return filename
