# for multiple documents 
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents = [
    "Delhi is capital of India.",
    "Mumbai is capital of Maharashtra.",
    "Paris is Capital of France.",
    "Peacock is national bird of India",
    "Hariyal is state bird of maharashtra"
]

result = embeddings.embed_documents(documents, dimensions=32)
print(result)
print(len(result))