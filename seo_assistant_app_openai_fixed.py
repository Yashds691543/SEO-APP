import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file or environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Prompt template
def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-4 only if you have access
            messages=[
                {"role": "system", "content": "You are an expert SEO assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🔍 LLM SEO Assistant")
    input_text = gr.Textbox(label="Enter your SEO Prompt")
    output_text = gr.Textbox(label="LLM Response", lines=10)
    generate_button = gr.Button("Generate Response")

    generate_button.click(fn=generate_response, inputs=[input_text], outputs=[output_text])

# Run the app
demo.launch()
