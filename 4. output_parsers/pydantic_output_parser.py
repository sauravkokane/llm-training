from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


class Person(BaseModel):
	name: str = Field(description="Name of the character")
	age: int | None = Field(gt=15, description="Age of the character")
	address: str = Field(description="Address of that character, or where does it came from.")
	basic_trait: Optional[str] = Field(description="General behavior or speciality of character")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
	template="Give me the name, age, address and basic trait or general behavior of fictional characters from writing of auther {writer} \n {format_instruction}",
	input_variables=['writer'],
	partial_variables={'format_instruction': parser.get_format_instructions()}
)


chain = template | model | parser


# print(f"# Prompt: {prompt}")

result = chain.invoke({'writer': "Aurther Conan Doyle"})

print(result) # name='Sherlock Holmes' age=34 address='221B Baker Street, London' basic_trait='Highly observant and intelligent'
print(type(result)) # # <class '__main__.Person'>


# Prompt: text='''Give me the name, age, address and basic trait or general behavior of fictional characters from writing of Pu. La. Deshpande 
# The output should be formatted as a JSON instance that conforms to the JSON schema below.

# # As an example, for the schema 
# {
# 	"properties": {
# 		"foo": {
# 			"title": "Foo", 
# 			"description": "a list of strings", 
# 			"type": "array", 
# 			"items": {
# 				"type": "string"
# 			}
# 		}
# 	}, 
# 	"required": ["foo"]
# }
# # the object 
# {
# 	"foo": ["bar", "baz"]
# } # is a well-formatted instance of the schema. 
# # The object 
# {"properties": {
# 	"foo": ["bar", "baz"]
# 	}
# } # is not well-formatted.

# # Here is the output schema:
# # ```
# {
# 	"properties": {
# 		"name": {
# 			"description": "Name of the character", 
# 			"title": "Name", 
# 			"type": "string"
# 		}, 
# 		"age": {
# 			"anyOf": [{
# 				"exclusiveMinimum": 15, 
# 				"type": "integer"
# 			}, {
# 				"type": "null"
# 			}], 
# 			"description": "Age of the character", 
# 			"title": "Age"
# 		}, 
# 		"address": {
# 			"description": "Address of that character, or where does it came from.", 
# 			"title": "Address", 
# 			"type": "string"
# 		}, 
# 		"basic_trait": {
# 			"anyOf":[
# 				{"type": "string"}, 
# 				{"type": "null"}
# 			], 
# 			"description": "General behavior or speciality of character", 
# 			"title": "Basic Trait"
# 		}
# 	}, 
# 	"required": [
# 		"name", 
# 		"age", 
# 		"address", 
# 		"basic_trait"
# 	]
# }
# ```
# Parsed_result: name='Rama Shembekar' age=45 address='Pune, Maharashtra, India' basic_trait='Sarcastic humor'
# <class '__main__.Person'>