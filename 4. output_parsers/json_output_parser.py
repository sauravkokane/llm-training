from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
	template="Give me the name, age and address of fictional characters from writing of {writer} \n {format_instruction}",
	input_variables=['writer'],
	partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser


result = chain.invoke({'writer': "Aurthor Conan Doyle"})

print(result)
print(type(result))



# Output:
# {
# 'characters': [{
# 		'name': 'Sherlock Holmes', 
# 		'age': '37', 
# 		'address': '221B Baker Street, London'
# 	}, 
# 	{
# 		'name': 'Dr. John Watson', 
# 		'age': '40', 
# 		'address': '221B Baker Street, London'
# 	}]
# }