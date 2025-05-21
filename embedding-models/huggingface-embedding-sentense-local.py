from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_home'

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device':'cpu'}

embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

sentence = "Mango is my favourite fruit."

result = embeddings.embed_query(sentence)
print(result)
print(len(result))
