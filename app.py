import gradio as gr
from cover_letter_utils import (
    extract_text_from_resume,
    generate_cover_letter,
    export_cover_letter_to_pdf
)

# ✅ Interface function
def cover_letter_interface(resume_file, job_description):
    if resume_file is None or job_description.strip() == "":
        return "❌ Please upload a resume and enter a job description."
    
    resume_text = extract_text_from_resume(resume_file)
    letter = generate_cover_letter(resume_text, job_description)
    pdf_path = export_cover_letter_to_pdf(letter)
    
    return letter, pdf_path

# ✅ Gradio UI
demo = gr.Interface(
    fn=cover_letter_interface,
    inputs=[
        gr.File(label="Upload Resume (PDF)", file_types=[".pdf"]),
        gr.Textbox(label="Job Description", placeholder="Paste job description here...")
    ],
    outputs=[
        gr.Textbox(label="Generated Cover Letter", lines=20),
        gr.File(label="📄 Download Cover Letter (PDF)")
    ],
    title="📄 AI Cover Letter Generator",
    description="Upload your resume and paste a job description to generate a tailored AI-powered cover letter.",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch()

