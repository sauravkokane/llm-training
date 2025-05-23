from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate.from_messages([
	('system', "You are a very helpful {domain} expert."),
	('human', "Explain me in simple terms, what is {topic}?")
])


prompt = chat_template.invoke({
	'domain': "Cricket",
	'topic': "LBW"
})


print(prompt)