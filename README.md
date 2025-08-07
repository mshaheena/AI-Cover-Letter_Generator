---
title: AI Cover Letter Generator
emoji: 💼
colorFrom: green
colorTo: green
sdk: gradio
sdk_version: 4.16.0
app_file: app.py
pinned: true
license: mit
---


# 🏢 AI Cover Letter Generator

Create a professional, tailored cover letter from your resume and job description using LLMs.

## ✨ Features
- Upload your **resume (PDF)**
- Paste the **job description**
- Select tone: Formal, Friendly, Creative
- Generates an **AI-powered cover letter** using FLAN-T5
- Preview + Download **cover letter as PDF**

## 🚀 Live Demo
[Try on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/cover-letter-generator)

## 📂 Sample Files
You can test with this sample resume:
- [`sample_resume.pdf`](./sample_resume.pdf) *(add yours here)*

## 🚜 How it Works
1. Extracts text from resume using `pdfplumber`
2. Generates cover letter using `transformers` pipeline
3. Wraps result in a styled PDF using `reportlab`

## ⚖️ License
This project is licensed under the [MIT License](LICENSE).

## 💼 Ideal For
- Portfolio Projects
- Freelancing Showcases
- Internship/Job Applications

---
Built with ❤️ by [Shaheena](https://www.linkedin.com/in/m-shaheena-967357313/)

