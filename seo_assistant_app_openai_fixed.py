import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are an AI SEO Assistant helping optimize web content.
Your goal is to improve ranking, keyword use, readability, and structure.

Input: {query}

Helpful SEO Feedback:
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

st.set_page_config(page_title="SEO Assistant")
st.title("🔍 Internal SEO Assistant")

user_input = st.text_area("Enter SEO content:", height=200)

if st.button("Generate SEO Suggestions"):
    if user_input:
        with st.spinner("Generating..."):
            response = chain.run(query=user_input)
            st.write(response)
    else:
        st.warning("Enter some text.")
