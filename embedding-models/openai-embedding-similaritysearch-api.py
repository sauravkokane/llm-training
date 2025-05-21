from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
"Water boils at 100 degrees Celsius at sea level.",
"The Earth revolves around the Sun once every 365.25 days.",
"Photosynthesis converts carbon dioxide into oxygen and glucose.",
"The mitochondrion is the powerhouse of the cell.",
"Light travels at approximately 299,792 kilometers per second.",
  

"Mount Everest is the highest mountain above sea level.",
"The Amazon River is the second longest river in the world.",
"Australia is both a continent and a country.",
"The Sahara is the largest hot desert on Earth.",
"Japan is located in the Pacific Ring of Fire.",
  

"William Shakespeare wrote Hamlet and Macbeth.",
"George Orwell’s 1984 explores themes of surveillance and control.",
"To Kill a Mockingbird was written by Harper Lee.",
"The novel Frankenstein was authored by Mary Shelley.",
"Poetry often uses metaphors and symbolism.",
"The term “stream of consciousness” is a literary technique.",
"Fyodor Dostoevsky wrote Crime and Punishment.",

"The Great Fire of London occurred in 1666.",
"World War II ended in 1945.",
"The Roman Empire collapsed in 476 AD.",
"Mahatma Gandhi led India’s non-violent independence movement.",
"The Berlin Wall fell in 1989.",
  

"Lionel Messi has won multiple Ballon d'Or awards.",
"The Olympics are held every four years.",
"Serena Williams dominated women’s tennis for decades.",
"Cricket is the most popular sport in India.",
"Basketball was invented by James Naismith.",
"A marathon is 42.195 kilometers long.",
  
"Bananas are rich in potassium.",
"The human body contains 206 bones.",
"Bees communicate using a waggle dance.",
"Glass is made primarily from sand.",
"Tomatoes are technically classified as fruits."]

query = "Tell me about Julius Caesar."


embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=300)

doc_embeddings = embeddings.embed_documents(documents)

# print(len(doc_embeddings))


query_embedding = embeddings.embed_query(query)

similarity_score = cosine_similarity([query_embedding], doc_embeddings)[0]
# print(similarity_score)

top_three = sorted(list(enumerate(similarity_score)), key=lambda x: x[1], reverse=True)[:3]
# print(top_three)

for i, (index, score) in enumerate(top_three):
	print(f"{i+1}. document: {documents[index]}, score: {score}")