from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17')

result = model.invoke("Tell me about national bird of India.")

print(result.content)
print(type(result))