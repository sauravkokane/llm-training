from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
	RunnableSequence, 
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

generation_chain = RunnableSequence(generationPrompt, model, parser)
summarization_chain = RunnableSequence(summarizationPrompt, model, parser)

branch_chain = RunnableBranch(
	(lambda x: len(x.split())>=300, summarization_chain),
	(RunnablePassthrough())
)

final_chain = RunnableSequence(generation_chain, branch_chain)

result= final_chain.invoke(dict(topic="Russia vs Ukraine War"))
print(result)


# OUTPUT1 = """
# 	Introduction:

# 	The ongoing conflict between Russia and Ukraine is a complex and multifaceted one, with roots dating back to the fall of the Soviet Union and the subsequent independence of Ukraine in 1991. The annexation of Crimea by Russia in 2014 and the ongoing fighting in Eastern Ukraine have only served to escalate tensions between the two countries and their respective allies.

# 	Background:

# 	The conflict between Russia and Ukraine can be traced back to the historical ties between the two countries. Ukraine was a key part of the Russian Empire for centuries until it gained independence in 1991. However, there has always been a strong Russian influence in Ukraine, particularly in the eastern regions of the country where a significant Russian-speaking population resides.

# 	In 2014, Russia annexed Crimea following a controversial referendum that was widely condemned by the international community. This move was seen as a violation of Ukraine's sovereignty and territorial integrity, leading to widespread condemnation and economic sanctions against Russia.

# 	Following the annexation of Crimea, pro-Russian separatists in Eastern Ukraine declared independence and began fighting against the Ukrainian government. The conflict quickly escalated into a full-blown war, with both sides accusing each other of violating ceasefires and committing human rights abuses.

# 	Examples of the Conflict:

# 	1. Annexation of Crimea: In February 2014, Russian forces seized control of Crimea, a strategic peninsula in the Black Sea that has long been of great importance to both Russia and Ukraine. The annexation was condemned by the international community, with many countries refusing to recognize Crimea as part of Russia.
# 	2. Fighting in Eastern Ukraine: The conflict in Eastern Ukraine has been ongoing since 2014, with both Ukrainian government forces and pro-Russian separatists engaging in heavy fighting in cities such as Donetsk and Luhansk. The conflict has resulted in thousands of deaths and displaced hundreds of thousands of people.

# 	3. Humanitarian Crisis: The conflict in Ukraine has led to a severe humanitarian crisis, with millions of people in need of assistance. Many have been forced to flee their homes and seek refuge in other parts of the country or in neighboring countries.

# 	4. International Involvement: The conflict has also drawn in other countries, with Russia providing support to the separatist forces in Eastern Ukraine and the West backing the Ukrainian government. This has led to a further escalation of the conflict and increased tensions between Russia and the West.

# 	Conclusion:

# 	The conflict between Russia and Ukraine is a complex and ongoing one that has deep historical roots and has resulted in significant human suffering. The annexation of Crimea and the fighting in Eastern Ukraine have only served to further escalate tensions between the two countries and their allies. A peaceful resolution to the conflict remains elusive, with both sides showing little willingness to compromise. Diplomatic efforts are ongoing, but the future remains uncertain for the people of Ukraine and the region as a whole.
# """



# OUTPUT2="""
# 	- The Russia vs Ukraine war, also known as the Russo-Ukrainian war, has been ongoing since 2014 and is considered a significant conflict in Europe.
# 	- The conflict began with political and social unrest in Ukraine, leading to the annexation of Crimea by Russia and a rebellion by pro-Russian separatists in eastern Ukraine.
# 	- Key events in the war include the downing of Malaysia Airlines flight MH17 and the Battle of Debaltseve.
# 	- Both sides have engaged in violent confrontations, leading to casualties, destruction, and human rights abuses.
# 	- International efforts to broker a ceasefire and end the conflict have been largely unsuccessful, with sporadic fighting continuing.
# 	- The conflict remains complex and volatile, with no clear resolution in sight. It is important for all parties involved to work towards a peaceful resolution to end the suffering of the civilian population and restore stability to the region.
# """



# CHAIN STRUCTURE:
#   +-------------+
#   | PromptInput |
#   +-------------+
#           *
#           *
#           *
# +----------------+
# | PromptTemplate |
# +----------------+
#           *
#           *
#           *
#   +------------+
#   | ChatOpenAI |
#   +------------+
#           *
#           *
#           *
# +-----------------+
# | StrOutputParser |
# +-----------------+
#           *
#           *
#           *
#     +--------+
#     | Branch |
#     +--------+
#           *
#           *
#           *
#   +--------------+
#   | BranchOutput |
#   +--------------+