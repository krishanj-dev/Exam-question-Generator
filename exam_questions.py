import nltk
nltk.download('punkt')

from transformers import pipeline
from keybert import KeyBERT
import gradio as gr
# Load T5 question generation pipeline
generator = pipeline("text-generation", model="valhalla/t5-small-qa-qg-hl")
kw_model = KeyBERT()

def extract_keywords(text):
    keywords = kw_model.extract_keywords(text, top_n=3)
    return [kw[0] for kw in keywords]
def generate_mcq(text):
    # Generate question
    q = generator(text, max_length=64, num_return_sequences=1)[0]['generated_text']

    # Extract keywords for options
    keywords = extract_keywords(text)
    options = keywords + ["Random distractor"]

    # Format output
    return {
        "Question": q,
        "Options": options,
        "Correct Answer": keywords[0] if keywords else "N/A"
    }


def ui_function(text):
    result = generate_mcq(text)
    return f"Q: {result['Question']}\n\nOptions:\nA) {result['Options'][0]}\nB) {result['Options'][1]}\nC) {result['Options'][2]}\nD) {result['Options'][3]}\n\nCorrect Answer: {result['Correct Answer']}"

iface = gr.Interface(
    fn=ui_function,
    inputs=gr.Textbox(lines=5, placeholder="Paste your lecture notes here..."),
    outputs="text",
    title="Exam Question Generator",
    description="Paste lecture notes → Get MCQs instantly!"
)

iface.launch()