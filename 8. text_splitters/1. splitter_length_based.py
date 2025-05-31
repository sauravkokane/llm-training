from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='D:\\Python Projects\\llm_training\\7. document_loaders\\azure-sdks.pdf')

splitter = CharacterTextSplitter(
	chunk_size=100,
	chunk_overlap=15, 	# 10% of chunk size
	separator=''
)

docs = loader.load()

result = splitter.split_documents(documents=docs)
print(len(result))

print("1. ", result[0].page_content)
print("2. ", result[1].page_content)
print("3. ", result[2].page_content)