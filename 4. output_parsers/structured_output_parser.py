from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


schema = [
	ResponseSchema(name='Fact_1', description="first fact about topic"),
	ResponseSchema(name='Fact_2', description="second fact about topic"),
	ResponseSchema(name='Fact_3', description="third fact about topic"),
	ResponseSchema(name='Fact_4', description="fourth fact about topic"),
	ResponseSchema(name='Fact_5', description="fifth fact about topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(template="Give 5 facts about characters from the writings of {author} \n {format_instructions}",
	input_variables = ['author'],
	partial_variables= {'format_instructions': parser.get_format_instructions()}
)



chain = template | model | parser

result = chain.invoke({'author': 'J K Rollings'})

print(result)


# Output:
# {
# 	'Fact_1': 'Harry Potter is an orphan who discovers he is a wizard on his eleventh birthday.', 
# 	'Fact_2': 'Hermione Granger is known for her intelligence and quick-thinking skills which help the trio in many dangerous situations.', 
# 	'Fact_3': 'Ron Weasley comes from a large family of magical blood and is known for his loyalty and sense of humor.', 
# 	'Fact_4': 'Albus Dumbledore is the headmaster of Hogwarts School of Witchcraft and Wizardry and is considered one of the greatest wizards of all time.', 
# 	'Fact_5': 'Severus Snape, despite his harsh demeanor, has a complex backstory and ultimately plays a crucial role in the defeat of Lord Voldemort.'
# }


# parser.get_format_instructions():
# The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":

# ```json
# {
# 	"Fact_1": string  // first fact about topic
# 	"Fact_2": string  // second fact about topic
# 	"Fact_3": string  // third fact about topic
# 	"Fact_4": string  // fourth fact about topic
# 	"Fact_5": string  // fifth fact about topic
# }