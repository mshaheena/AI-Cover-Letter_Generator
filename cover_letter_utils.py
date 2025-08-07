import pdfplumber
from transformers import pipeline
from reportlab.pdfgen import canvas

# Load summarization pipeline
summarizer = pipeline("summarization")

def extract_text_from_resume(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def generate_cover_letter(resume_text, job_description):
    try:
        combined_input = (
            f"Resume: {resume_text[:1000]}\n\nJob Description: {job_description}\n\n"
            "Generate a professional and personalized cover letter."
        )
        summary = summarizer(combined_input, max_length=180, min_length=60, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"⚠️ Failed to generate cover letter: {str(e)}"

def export_cover_letter_to_pdf(text, filename="cover_letter.pdf"):
    c = canvas.Canvas(filename)
    textobject = c.beginText(50, 750)
    textobject.setFont("Helvetica", 12)

    for line in text.split('\n'):
        textobject.textLine(line)
    c.drawText(textobject)
    c.save()
    return filename
