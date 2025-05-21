from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_home'

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device':'cpu'}

embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

documents = [
    "Delhi is capital of India.",
    "Mumbai is capital of Maharashtra.",
    "Paris is Capital of France.",
    "Peacock is national bird of India",
    "Hariyal is state bird of maharashtra"
]

result = embeddings.embed_documents(documents)
print(result)
print(len(result))
