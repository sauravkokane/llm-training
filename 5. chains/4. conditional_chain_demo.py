# import all necessary classes
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv

# load environment variables
load_dotenv()


class Feedback(BaseModel):
	sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of feedback as it is positive or negative")
	
# create parser
parser = StrOutputParser()
output_parser = PydanticOutputParser(pydantic_object=Feedback)

# create models
model = ChatOpenAI()



# create prompts
reviewSentimentPrompt = PromptTemplate(
	template="Classify the following sentiment of following feedback into positive or negative \n{feedback} \n{format_instructions}",
	input_variables=['feedback'],
	partial_variables={'format_instructions': output_parser.get_format_instructions()}
)

positiveActionPrompt = PromptTemplate(
	template="Write a appropriate response to the given positive feedback: \n{feedback}",
	input_variables=['feedback'],
)

negativeActionPrompt = PromptTemplate(
	template="Write a appropriate response to the given negative feedbace: \n{feedback}",
	input_variables=['feedback'],
)

classifier_chain = reviewSentimentPrompt | model | output_parser

branch_chain = RunnableBranch(
	(lambda x: x.sentiment=='positive', positiveActionPrompt | model | parser),
	(lambda x: x.sentiment=='negative', negativeActionPrompt | model | parser),
	RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain



result = chain.invoke({'feedback': "This is very bad phone. I will not recommend this to anyone."})
print(result) # Thank you so much for your kind words! I'm thrilled to hear that you had a positive experience. Let me know if there's anything else I can help you with.
# I’m sorry to hear that you didn’t have a positive experience. Your feedback is important to us and we’ll use it to improve our services. Thank you for sharing your thoughts with us.

# chain.get_graph().print_ascii()


#     +-------------+
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#      +------------+
#      | ChatOpenAI |
#      +------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+