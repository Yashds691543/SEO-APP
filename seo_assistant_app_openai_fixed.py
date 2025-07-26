import gradio as gr
from openai import OpenAI
import os

# Get your API key from Hugging Face secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_seo(content):
    prompt = f"""You are an expert SEO assistant. Improve this content for better ranking:
    
    {content}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

iface = gr.Interface(
    fn=optimize_seo,
    inputs=gr.Textbox(lines=10, placeholder="Paste your content here..."),
    outputs="text",
    title="LLM SEO Optimizer",
    description="Enter any blog or web content, and this app will rewrite it with better SEO quality using GPT-4."
)

if __name__ == "__main__":
    iface.launch()
