import gradio as gr
from cover_letter_utils import (
    extract_text_from_resume,
    generate_cover_letter,
    export_cover_letter_to_pdf
)

generated_text = ""

def generate(resume_pdf, job_description):
    global generated_text
    resume_text = extract_text_from_resume(resume_pdf.name)
    generated_text = generate_cover_letter(resume_text, job_description)
    return generated_text

def download_pdf():
    if generated_text:
        file_path = export_cover_letter_to_pdf(generated_text)
        return file_path

with gr.Blocks(css="style.css") as demo:
    gr.Markdown("## 📝 AI Cover Letter Generator")
    gr.Markdown("Upload your resume and paste a job description to generate a tailored AI-powered cover letter.")

    with gr.Row():
        with gr.Column(scale=1):
            resume_file = gr.File(label="📂 Upload Resume (PDF)", file_types=[".pdf"])
            job_desc = gr.Textbox(lines=3, placeholder="Job Description", label="💼 Job Description")
            submit_btn = gr.Button("🚀 Submit", variant="primary")
            clear_btn = gr.Button("🧹 Clear", variant="secondary")

        with gr.Column(scale=1):
            output_letter = gr.Textbox(label="📄 Generated Cover Letter", lines=18)
            download_btn = gr.Button("📥 Download Cover Letter (PDF)")

    submit_btn.click(generate, inputs=[resume_file, job_desc], outputs=[output_letter])
    download_btn.click(download_pdf, outputs=[])

    clear_btn.click(lambda: ("", "", ""), inputs=[], outputs=[resume_file, job_desc, output_letter])

demo.launch()
