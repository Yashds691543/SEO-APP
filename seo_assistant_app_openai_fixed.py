import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are an expert SEO assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## 🔍 LLM SEO Assistant")
    input_text = gr.Textbox(label="Enter your SEO Prompt")
    output_text = gr.Textbox(label="LLM Response", lines=10)
    generate_button = gr.Button("Generate Response")

    generate_button.click(fn=generate_response, inputs=[input_text], outputs=[output_text])

demo.launch()
