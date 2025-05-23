from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
	SystemMessage(content="You are a very helpful assistant.")
]

while True:
	user_input = input("You: ")
	chat_history.append(HumanMessage(content=user_input))
	if user_input == 'exit':
		print("****Thank you for using my service.****")
		break
	result = model.invoke(chat_history)
	chat_history.append(AIMessage(content=result.content))

	print(f"Bot: {result.content}")

print(chat_history)