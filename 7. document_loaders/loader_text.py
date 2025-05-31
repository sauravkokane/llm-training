from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
	template="Write a summary for following text. \n{text}",
	input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader(file_path="example.txt", encoding='utf-8')

docs = loader.load()

# print(f"Type of Docs: {type(docs)}") # <class 'list'>
# print(f"length of Docs: {len(docs)}") # 1
# print(f"Type of Doc: {type(docs[0])}") # <class 'langchain_core.documents.base.Document'>
# print(f"First Doc: {docs[0]}")

chain = prompt | model | parser

result = chain.invoke(dict(text=docs[0].page_content))

print(result)


# [Document(
# metadata={'source': 'example.txt'}, 
# page_content='''Memory management is always  an extremely important part of any program or application being developed in the Java
# programming language. Whenever objects are created for classes in any programs or applications developed using Java language,
# they are allocated a certain amount of memory allowing the program or application to function the way that it should.
# \tJust like objects in Java, variables and objects need to be assigned or allocated certain areas of memory to ensure that they can be used
# without errors or exceptions manifesting themselves. However, the memory that is allocated to them differs according to the
# scope that the said variable is located in.
# Once the memory allocated to a certain variable or object is deemed useless and the purpose of the variable or object has
# been completed, it is important for the allocated memory to be recycled and be usable for other purposes. And that is where
# the garbage collector in Java comes into play.
# Fortunately for the Java programming language, memory reclamation is automatic in the Java vitual machine
# (JVM), which means that Java developers do not necessarily have to go out of their way in order to free memory objects that''')]
