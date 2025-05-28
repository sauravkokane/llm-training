from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
	RunnableSequence, 
	RunnableParallel, 
	RunnablePassthrough, 
	RunnableLambda
)
from dotenv import load_dotenv

load_dotenv()

def word_count(text:str):
	words = text.split()
	return len(words)

generationPrompt = PromptTemplate(
	template="Tell me a  joke about {topic}",
	input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

generation_chain = RunnableSequence(generationPrompt, model, parser)

parallel_chain = RunnableParallel({
	'joke': RunnablePassthrough(),
	'count': RunnableLambda(func=word_count)
})

chain = RunnableSequence(generation_chain, parallel_chain)

result = chain.invoke(dict(topic="AI"))

print(result)
{
	'joke': '''
	Why was the robot bad at tennis?
	Because it had a hard drive!
	''', 
	'count': 13
}



#               +-------------+
#               | PromptInput |
#               +-------------+
#                       ||
#                       ||
#                       \/
#              +----------------+
#              | PromptTemplate |
#              +----------------+
#                       ||
#                       ||
#                       \/
#                +------------+
#                | ChatOpenAI |
#                +------------+
#                       ||
#                       ||
#                       \/
#             +-----------------+
#             | StrOutputParser |
#             +-----------------+
#                       ||
#                       ||
#                       \/
#        +---------------------------+
#        | Parallel<joke,count>Input |
#        +---------------------------+
#               //              \\
#              //                \\ 
#             \./                \./
# +-------------+              +------------+
# | Passthrough |              | word_count |
# +-------------+              +------------+
#              \\                //
#               \\              //
#               \./            \./
#        +----------------------------+
#        | Parallel<joke,count>Output |
#        +----------------------------+