from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

generationPrompt = PromptTemplate(
	template="Tell me a  joke about {topic}",
	input_variables=['topic']
)

explainationPrompt = PromptTemplate(
	template = "Explain me the following joke \n{joke}",
	input_variables=['joke']
)

model = ChatOpenAI()

parser = StrOutputParser()

generation_chain = RunnableSequence(generationPrompt, model, parser)

explaination_chain = RunnableSequence(explainationPrompt, model, parser)


parallel_chain = RunnableParallel({
	'joke': RunnablePassthrough(),
	'explaination': explaination_chain
})

chain = RunnableSequence(generation_chain, parallel_chain)
result = chain.invoke(dict(topic="Cricket"))

print(result)

# {
# 	'joke': """
# 	Why did the cricket team go to the bakery?
# 	Because they needed a good opener!
# 	""", 
# 	'explaination': """
# 	In cricket, an "opener" is a term used to describe the first two batsmen in the batting line-up. They are responsible for facing the first balls of the innings and setting a good foundation for the rest of the team. 
# 	So, in this joke, the cricket team went to the bakery looking for a "good opener" referring to a quality batsman to start their innings. It's a play on words as "opener" can also refer to someone or something that starts or opens something up.
# 	"""
# }


#                   +-------------+
#                   | PromptInput |
#                   +-------------+
#                           ||
#                           ||
#                 +----------------+
#                 | PromptTemplate |
#                 +----------------+
#                           ||
#                           ||
#                   +------------+
#                   | ChatOpenAI |
#                   +------------+
#                           ||
#                           ||
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           ||
#                           ||
#         +----------------------------------+
#         | Parallel<joke,explaination>Input |
#         +----------------------------------+
#                  //              \\
#                 //                \\
#                //                  \\
#               //                    \\
# +----------------+                   \\
# | PromptTemplate |                    ||
# +----------------+                    ||
#           ||                          ||
#           ||                          ||
#           ||                          ||
#   +------------+                      ||
#   | ChatOpenAI |                      ||
#   +------------+                      ||
#           ||                          ||
#           ||                          ||
#           ||                          ||
# +-----------------+               +-------------+
# | StrOutputParser |               | Passthrough |
# +-----------------+               +-------------+
#                  \\                  //
#                   \\                //
#                    \\              //
#        +-----------------------------------+
#        | Parallel<joke,explaination>Output |
#        +-----------------------------------+