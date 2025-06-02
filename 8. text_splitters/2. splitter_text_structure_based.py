from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='D:/Python Projects/llm_training/7. document_loaders/data/Bharatiya Sakshya Adhiniyam, 2023.pdf')

splitter = RecursiveCharacterTextSplitter(
	chunk_size=160,
	chunk_overlap=0,
	separators=["\n\n", "\n", ' ', '']
)

docs = loader.load()


result = splitter.split_documents(documents=docs[19:21])
print(len(result))


for i, r in enumerate(result[:20]):
	print([i], (r.page_content))

"""The realm of Artificial Intelligence is no longer confined to science fiction; it's rapidly 
transforming the way we build and interact with applications. Microsoft Azure stands 
at the forefront of this revolution, offering a rich suite of AI services capable of 
understanding language, recognizing images, making predictions, and much more. For 
developers eager to harness this power, Software Development Kits (SDKs) are the 
indispensable keys that unlock the door to intelligent innovation. Think of Azure AI as a 
vast, intricate machine, and the SDKs as the specialized tools you need to operate 
each part with precision and ease. This guide will navigate you through the galaxy of 
Azure AI SDKs, explaining what they are, what they do, and why this multi-faceted 
approach is the secret to efficient AI development.
"""