# 📘 Exam Question Generator

This project is a simple **MCQ generator** built with **Python, Hugging Face Transformers, KeyBERT, and Gradio**.  
It takes lecture notes as input and automatically generates a **question with multiple-choice options**.

---

## 🚀 Features
- **[Question generation](ca://s?q=Question_generation_with_T5_model)** using a pretrained T5 model.  
- **[Keyword extraction](ca://s?q=Keyword_extraction_with_KeyBERT)** for distractor options.  
- **[Interactive UI](ca://s?q=Gradio_UI_for_exam_question_generator)** built with Gradio.  
- Generates **one MCQ per input paragraph**.  

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
pip install transformers datasets sentencepiece
pip install nltk spacy keybert gradio
