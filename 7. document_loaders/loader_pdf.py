from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(file_path='./azure-sdks.pdf', extract_images=False, )

data = loader.load()

print(data[8])
print(data[8].page_content)
print(data[8].metadata)