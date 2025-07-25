import streamlit as st
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os


os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=st.secrets["OPENAI_API_KEY"]
)

from langchain_openai import ChatOpenAI
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-4",
    client=client
)

# Prompt template
template = """You are an AI SEO Assistant helping optimize web content for better visibility in both traditional search engines (like Google) and AI-generated responses (like ChatGPT).

Analyze the article content and return:

1. A concise page title (≤60 characters)
2. A meta description (150–160 characters)
3. 3–5 FAQs
4. Long-tail keyword suggestions (at least 4)

Format with section headers:
- Title:
- Meta Description:
- FAQs:
- Keyword Suggestions:

Here is the article content:
{content}
"""

prompt = PromptTemplate(input_variables=["content"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit interface
st.set_page_config(page_title="LLM SEO Assistant", layout="centered")
st.title("🔍 Internal SEO Assistant (LLM-Powered)")

st.markdown("""
This tool generates SEO-optimized titles, meta descriptions, FAQs, and keywords using AI.
""")

with st.form("seo_form"):
    content = st.text_area("📄 Paste your article content:", height=300)
    submit = st.form_submit_button("🚀 Generate SEO Suggestions")

if submit and content:
    with st.spinner("Generating..."):
        result = chain.run(content=content)
        st.markdown("### ✅ SEO Suggestions:")
        st.code(result, language="markdown")
elif submit:
    st.error("Please paste your content.")
