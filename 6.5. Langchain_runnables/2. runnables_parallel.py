from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
	template="Write a tweet about {topic}",
	input_variables=['topic']
)
prompt2 = PromptTemplate(
	template="Write a LinkedIn post about {topic}",
	input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableParallel({
	'tweet': RunnableSequence(prompt1, model, parser),
	'linkedin_post': RunnableSequence(prompt2, model, parser)
})

result = chain.invoke(dict(topic='AI agents'))

print(result)
print(type(result))


chain.get_graph().print_ascii()


{
	'tweet': 
	"""
		AI agents are revolutionizing the way we interact with technology, making tasks more efficient and personalized. Excited to see where this incredible technology takes us next! #AI #innovation
	""", 
	'linkedin_post': 
	"""
		Exciting news in the world of Artificial Intelligence! AI agents are revolutionizing the way businesses operate by streamlining processes, personalizing experiences, and improving decision-making. These intelligent agents are capable of performing tasks autonomously, learning from data, and adapting to new information in real-time.
		I have had the privilege of witnessing firsthand the impact of AI agents in various industries, from customer service and marketing to healthcare and finance. The results speak for themselves – increased efficiency, enhanced productivity, and greater customer satisfaction.
		As we continue to push the boundaries of AI technology, the possibilities are truly endless. I am thrilled to be a part of this transformative journey and look forward to seeing how AI agents will shape the future of business. If you are interested in learning more about AI agents and their potential applications, feel free to reach out to me. Let's embrace the power of artificial intelligence together! #artificialintelligence #AIagents #innovation #futureofbusiness
	"""
}

