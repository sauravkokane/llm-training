from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


chat_template = ChatPromptTemplate([
	SystemMessage(content="You are a very helpful {domain} expert."),
	HumanMessage(content="Explain me in simple terms, what is {topic}?")
])


prompt = chat_template.invoke({
	'domain': "Cricket",
	'topic': "LBW"
})


print(prompt)