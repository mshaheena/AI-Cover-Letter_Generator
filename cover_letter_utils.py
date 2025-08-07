# cover_letter_utils.py
import pdfplumber
import re
from transformers import pipeline
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

summarizer = pipeline("summarization")
text_generator = pipeline("text-generation", model="google/flan-t5-large")

def extract_text_from_resume(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def generate_cover_letter(resume_text, job_description, tone="Formal"):
    prompt = f"""
You are an expert career assistant. Generate a {tone.lower()} cover letter using the resume and job description below.

Resume:
{resume_text}

Job Description:
{job_description}

Cover Letter:
"""
    result = text_generator(prompt, max_length=512, do_sample=False, temperature=0.7)[0]['generated_text']
    letter = result.split("Cover Letter:")[-1].strip()
    return letter

def export_cover_letter_to_pdf(cover_text, output_path="cover_letter.pdf"):
    c = canvas.Canvas(output_path, pagesize=LETTER)
    width, height = LETTER

    # Margin and line setup
    x_margin = 72
    y = height - 72
    lines = cover_text.split("\n")
    for line in lines:
        for wrapped_line in wrap_text(line, 80):
            if y < 72:
                c.showPage()
                y = height - 72
            c.drawString(x_margin, y, wrapped_line)
            y -= 14

    c.save()
    return output_path

def wrap_text(text, width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= width:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines
