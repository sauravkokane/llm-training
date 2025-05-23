from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
	('system', "You are a very helpful customer support agent."),
	MessagesPlaceholder("chat_history"),
	('user', "{query}")
])

# load chat history
chat_history = []
with open("chat_history.txt", 'r') as file:
	chat_history.extend(file.readlines())
print(chat_history)

# create prompt
prompt = chat_template.invoke({
	'chat_history': chat_history,
	'query': "Where is my refund"
})

print(prompt)