from huggingface_hub import login
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
import os

load_dotenv()

login(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

repo_id = "meta-llama/Llama-3.2-3B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task = 'text-generation',
    max_length=128,
    temperature=0.5,
)

model = ChatHuggingFace(llm=llm)


# 1st prompt -> detailed report
template1 = PromptTemplate(
	template="Write a detailed report on {topic}",
	input_variables=['topic']
)


# 2nd prompt -> summary
template2 = PromptTemplate(
	template="Write a pipeline summary on following text: \n{text}",
	input_variables=['text']
)


prompt1 = template1.invoke({'topic': "black hole"})

detailed_report = model.invoke(prompt1)


prompt2 = template2.invoke({'text': detailed_report.content})


summary = model.invoke(prompt2)


print(detailed_report)
print(summary.content)
