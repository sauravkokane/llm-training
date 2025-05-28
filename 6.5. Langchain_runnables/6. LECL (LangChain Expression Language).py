from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
	# RunnableSequence, 
	RunnableParallel, 
	RunnablePassthrough, 
	RunnableLambda,
	RunnableBranch
)
from dotenv import load_dotenv

load_dotenv()

def word_count(text:str):
	words = text.split()
	return len(words)

generationPrompt = PromptTemplate(
	template="write a detailed report on {topic} with examples",
	input_variables=['topic']
)

summarizationPrompt = PromptTemplate(
	template="Summarize the following text in few points. \n{text}",
	input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

generation_chain = generationPrompt | model | parser
summarization_chain = summarizationPrompt | model | parser

branch_chain = RunnableBranch(
	(lambda x: len(x.split())>=300, summarization_chain),
	(RunnablePassthrough())
)

final_chain = generation_chain | branch_chain

result= final_chain.invoke(dict(topic="Russia vs Ukraine War"))
print(result)

# final_chain.get_graph().print_ascii()

#  The Russia vs Ukraine War started in 2014 following Russia's annexation of Crimea and its support for separatist rebels in eastern Ukraine.
# - The conflict has led to a humanitarian crisis in the region, with thousands of civilians killed and displaced, and both sides accused of committing human rights abuses.
# - Key developments include the annexation of Crimea, the conflict in eastern Ukraine, the signing of the Minsk Agreements, and the resulting humanitarian crisis.
# - The war has strained relations between Russia and the West, with sanctions imposed on Moscow, and raised questions about the future of international security in Eastern Europe.
# - The international community must work towards a peaceful resolution to the conflict to prevent further violence and suffering in Ukraine.


#   +-------------+
#   | PromptInput |
#   +-------------+
#         ||
#         ||
#         \/
# +----------------+
# | PromptTemplate |
# +----------------+
#         ||
#         ||
#         \/
#   +------------+
#   | ChatOpenAI |
#   +------------+
#         ||
#         ||
#         \/
# +-----------------+
# | StrOutputParser |
# +-----------------+
#         ||
#         ||
#         \/
#     +--------+
#     | Branch |
#     +--------+
#         ||
#         ||
#         \/
#   +--------------+
#   | BranchOutput |
#   +--------------+