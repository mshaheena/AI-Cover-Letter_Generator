# app.py
import gradio as gr
from cover_letter_utils import extract_text_from_resume, generate_cover_letter, export_cover_letter_to_pdf
import tempfile

# Custom theme settings
theme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="gray",
    font=["Fira Code", "Arial", "sans-serif"]
).set(
    button_primary_background="linear-gradient(to right, #10b981, #059669)",
    button_primary_text_color="white",
    block_border_radius="16px"
)

def process_resume(resume_pdf, job_description, tone):
    if resume_pdf is None or job_description.strip() == "":
        return "Please upload a resume and enter job description.", None

    resume_text = extract_text_from_resume(resume_pdf.name)
    cover_letter = generate_cover_letter(resume_text, job_description, tone)

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        export_cover_letter_to_pdf(cover_letter, tmp.name)
        return cover_letter, tmp.name

with gr.Blocks(theme=theme) as demo:
    gr.Markdown("""
    # 💼 AI Cover Letter Generator
    Upload your **resume** and **job description**. Get a professional **AI-generated cover letter** instantly with optional tone selection!
    """)

    with gr.Row():
        resume_input = gr.File(label="Upload Your Resume (PDF)", file_types=[".pdf"])
        tone_input = gr.Radio(["Formal", "Friendly", "Creative"], value="Formal", label="Tone")

    job_desc_input = gr.Textbox(label="Paste Job Description", lines=6, placeholder="Enter the job description here...")

    generate_btn = gr.Button("✨ Generate Cover Letter")

    output_text = gr.Textbox(label="AI-Generated Cover Letter", lines=12)
    download_file = gr.File(label="Download PDF")

    generate_btn.click(
        fn=process_resume,
        inputs=[resume_input, job_desc_input, tone_input],
        outputs=[output_text, download_file]
    )

if __name__ == "__main__":
    demo.launch()
