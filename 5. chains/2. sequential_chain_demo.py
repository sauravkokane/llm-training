# Import required libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create detailed report prompt template
reportPromptTemplate = PromptTemplate(
	template="Genearate a detailed report on {topic}",
	input_variables=['topic']
)

# Create five point summary prompt template
summaryPromptTemplte = PromptTemplate(
	template="Genearate 5 point summary from the following text \n{text}",
	input_variables = ['text']
)

# Create parser
parser = StrOutputParser()

# Create model
model = ChatOpenAI()

# Create chain
chain = reportPromptTemplate | model | parser | summaryPromptTemplte | model | parser

# Generate result
result = chain.invoke({'topic': "India's Unemployment"})

# Print result
print(result)
