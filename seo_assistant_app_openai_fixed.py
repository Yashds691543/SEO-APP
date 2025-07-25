import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Set up the OpenAI API key from secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Initialize the LLM (GPT-4)

llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

# Set page title and layout
st.set_page_config(page_title="SEO Assistant", layout="centered")

# Title and intro
st.title("🔍 Internal SEO Assistant")
st.markdown("Ask anything SEO-related and get smart suggestions from GPT-4.")

# Input from user
user_input = st.text_area("📝 Enter your SEO query or content to optimize:", height=200)

# Prompt Template
template = """
You are an AI SEO Assistant helping optimize web content.
Your goal is to improve ranking, keyword use, readability, and structure.
Provide clear, actionable feedback. If a URL or HTML is provided, evaluate SEO best practices.

Input: {query}

Helpful SEO Feedback:
"""

prompt = PromptTemplate(
    input_variables=["query"],
    template=template
)

# Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Submit button
if st.button("Generate SEO Suggestions"):
    if user_input.strip():
        with st.spinner("Analyzing with GPT-4..."):
            response = chain.run(query=user_input)
            st.subheader("🔧 Optimized SEO Suggestions:")
            st.write(response)
    else:
        st.warning("Please enter some text to optimize.")
