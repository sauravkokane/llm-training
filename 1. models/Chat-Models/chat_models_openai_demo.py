from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4', max_tokens=200, temperature=0.7)

result = model.invoke("what is best in Mumbai?", )
print(result)