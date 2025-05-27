from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# create a template
template = PromptTemplate(
	template="Get character names and information from the writing of author: {author}.",
	input_variables=['author'],
)

# create a parser
parser = StrOutputParser()

# create a model
model = ChatOpenAI()

# create a chain
chain = template | model | parser

# visualize the chain
chain.get_graph().print_ascii()

# invoke a chain
result = chain.invoke({'author': "J K Rollings"})

#print a result
print(result)




#      +-------------+
#      | PromptInput |
#      +-------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#       +------------+
#       | ChatOpenAI |
#       +------------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+

# 1. Harry Potter - The main protagonist of the Harry Potter series, a young wizard who attends Hogwarts School of Witchcraft and Wizardry.

# 2. Hermione Granger - Harry's close friend and fellow Gryffindor student, known for her intelligence, bravery, and loyalty.

# 3. Ron Weasley - Harry's other close friend and fellow Gryffindor student, known for his humor, loyalty, and red hair.

# 4. Albus Dumbledore - The headmaster of Hogwarts and a powerful wizard who is also a mentor to Harry.

# 5. Severus Snape - The Potions Master at Hogwarts who has a complicated relationship with Harry and is revealed to have a complex backstory.

# 6. Lord Voldemort (Tom Riddle) - The main antagonist of the series, a dark wizard who seeks to conquer the wizarding world and defeat Harry.

# 7. Draco Malfoy - A Slytherin student who initially serves as a rival to Harry but ultimately shows some complexity and growth throughout the series.

# 8. Sirius Black - Harry's godfather and a member of the Order of the Phoenix, known for his loyalty and bravery.

# 9. Luna Lovegood - A Ravenclaw student known for her quirky personality and belief in magical creatures.

# 10. Bellatrix Lestrange - A loyal follower of Voldemort and a sadistic Death Eater who causes chaos and destruction throughout the series.
