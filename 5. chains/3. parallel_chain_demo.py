# import all necessary classes
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema.runnable import RunnableParallel
# from pydantic import BaseModel, Field
# from typing import Optional, Literal
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# create output schemas
schema = [
	ResponseSchema(name='Question 1', description='First Question of the quiz', type='string'),
	ResponseSchema(name='Question 2', description='Second Question of the quiz', type='string'),
	ResponseSchema(name='Question 3', description='Third Question of the quiz', type='string'),
	ResponseSchema(name='Question 4', description='Fourth Question of the quiz', type='string'),
	ResponseSchema(name='Question 5', description='Fifth Question of the quiz', type='string'),
]


# create parsers
notes_parser = StrOutputParser()
quiz_parser = StructuredOutputParser.from_response_schemas(schema)


# create prompts
notesPrompt = PromptTemplate(
	template="Generate short and simple notes from follwing text \n{text}",
	input_variables=['text']
)

quizPrompt = PromptTemplate(
	template="Generate 5 short question-answers from the follwing text \n{text} \n{format_instructions}",
	input_variables=['text'],
	partial_variables={'format_instructions': quiz_parser.get_format_instructions()}
)

mergePrompt = PromptTemplate(
	template="""
	Merge the provided notes and quiz into one document. 
	notes->
	'''
	{notes}
	'''
	and 
	quiz->
	'''
	{quiz}
	'''
""",
input_variables=['notes', 'quiz']
)


# create LLMs [Optional]

# Load models
notes_model = ChatOpenAI()
quiz_model =  ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")


# create chains
parallel_chains = RunnableParallel({
	'notes': notesPrompt | notes_model | notes_parser,
	'quiz': quizPrompt | quiz_model | quiz_parser
})

merge_chain = mergePrompt | notes_model | notes_parser

# create chain
chain = parallel_chains | merge_chain

# invoke chains
text = """
A Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression. It finds the optimal hyperplane (or line) to separate data points into different classes, maximizing the margin between the closest data points of each class, according to ScienceDirect and IBM. SVMs are known for their effectiveness in high-dimensional spaces and complex decision boundaries. 
Key Concepts:
Hyperplane:
A decision boundary that separates data points into different classes. In 2D, it's a line; in 3D, it's a plane; and in higher dimensions, it's a hyperplane.
Support Vectors:
Data points that are closest to the hyperplane and determine its location.
Margin:
The distance between the hyperplane and the closest data points of each class.
Optimal Hyperplane:
The hyperplane that maximizes the margin and provides the best separation between classes. 
How SVM Works:
1. Data Representation:
SVMs represent data points as vectors in an n-dimensional space.
2. Finding the Optimal Hyperplane:
SVMs use optimization techniques to find the hyperplane that best separates the data points.
3. Maximizing the Margin:
The goal is to find the hyperplane that maximizes the margin between the closest data points of different classes.
4. Prediction:
Once the optimal hyperplane is found, new data points are classified by determining which side of the hyperplane they fall on. 
Advantages of SVM:
Effective in high-dimensional spaces: SVMs can handle datasets with many features. 
Can model complex decision boundaries: SVMs can effectively handle nonlinear data using kernel methods. 
Less prone to overfitting: SVMs tend to generalize well to new data compared to some other algorithms. 
Applications of SVM:
Classification: Identifying different classes or categories in data.
Regression: Predicting continuous values.
Anomaly detection: Identifying unusual data points. 
"""
result = chain.invoke({'text':text})

# print result
print(result)


print("finised")

# *** Output ***:
# - SVM is a supervised machine learning algorithm for classification and regression.
# - It finds the optimal hyperplane to separate data points, maximizing the margin.
# - Key concepts include hyperplane, support vectors, and margin.
# - SVM works by representing data points as vectors and finding the optimal hyperplane.
# - Advantages include effectiveness in high-dimensional spaces and handling complex decision boundaries.
# - Applications include classification, regression, and anomaly detection.

# Quiz:
# - What is a Support Vector Machine (SVM) used for?
# Answer: Classification and regression.
# - What is a hyperplane in the context of SVM?
# Answer: A decision boundary that separates data points into different classes.
# - What are support vectors?
# Answer: Data points that are closest to the hyperplane and determine its location.
# - What is the goal of SVM in terms of the margin?
# Answer: To find the hyperplane that maximizes the margin between the closest data points of different classes.
# - Name one advantage of using SVMs.
# Answer: Effective in high-dimensional spaces or can model complex decision boundaries or less prone to overfitting.
# *** Chain structure ***:

#              +---------------------------+
#              | Parallel<notes,quiz>Input |
#              +---------------------------+
#                   ***               ***
#                ***                     ***
#              **                           **
# +----------------+                   +----------------+
# | PromptTemplate |                   | PromptTemplate |
# +----------------+                   +----------------+
#           *                                   *
#           *                                   *
#           *                                   *
#   +------------+                 +------------------------+
#   | ChatOpenAI |                 | ChatGoogleGenerativeAI |
#   +------------+                 +------------------------+
#           *                                   *
#           *                                   *
#           *                                   *
# +-----------------+              +------------------------+
# | StrOutputParser |              | StructuredOutputParser |
# +-----------------+              +------------------------+
#                   ***               ***
#                      ***         ***
#                         **     **
#              +----------------------------+
#              | Parallel<notes,quiz>Output |
#              +----------------------------+
#                             *
#                             *
#                             *
#                    +----------------+
#                    | PromptTemplate |
#                    +----------------+
#                             *
#                             *
#                             *
#                      +------------+
#                      | ChatOpenAI |
#                      +------------+
#                             *
#                             *
#                             *
#                   +-----------------+
#                   | StrOutputParser |
#                   +-----------------+
#                             *
#                             *
#                             *
#                +-----------------------+
#                | StrOutputParserOutput |
#                +-----------------------+
