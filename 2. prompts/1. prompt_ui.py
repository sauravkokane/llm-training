from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
from gen_utils import *
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-4', max_tokens=512)



st.header("Research Tool")
research_paper = st.selectbox("Select research paper name:", options=research_papers_list)

explanation_style = st.selectbox("Select style of explanation:", options=input_styles)

output_length = st.selectbox("Select depth of explanation:", options=input_lengths)

template = load_prompt("D:\\Python Projects\\llm_training\\2. prompts\\my_template.json")
prompt = template.invoke(
	dict(paper_input=research_paper, 
	style_input=explanation_style,
	length_input=output_length)
)


if st.button("Summarize"):
	result = model.invoke(prompt)
	st.markdown(result.content)
	# st.latex(render_latex(result.content))
