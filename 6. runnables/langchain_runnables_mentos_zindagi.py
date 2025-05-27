from abc import ABC, abstractclassmethod
from warnings import warn

import random

class Runnable(ABC):
    @abstractclassmethod
    def invoke(input_data):
        pass

class NakliLLM(Runnable):
    def __init__(self) -> None:
        print("LLM created")

    def predict(self, prompt):
        warn("predict method is being depricated in upcoming versions. For proper execution of code use invoke method", DeprecationWarning)

        response_list = [
            "Prague is very good city.",
            "Virat Kohli is a cricket player",
            "Mumbai is famous for its street food"
        ]
        return {'response': random.choice(response_list)}

    def invoke(self, prompt):
        response_list = [
            "Prague is very good city.",
            "Virat Kohli is a cricket player",
            "Mumbai is famous for its street food"
        ]
        return {'response': random.choice(response_list)}

class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables=[], partial_variables={}):
        self.template = template
        self.input_variables = input_variables
        self.partial_variables = partial_variables
    def format(self, input_dict):
        warn("format method is being depricated in upcoming versions. For proper execution of code use invoke method", DeprecationWarning)
        input_dict.update(self.partial_variables)
        return self.template.format(**input_dict)

    def invoke(self, input_dict):
        input_dict.update(self.partial_variables)
        return self.template.format(**input_dict)

    def __str__(self):
        return self.template

class RunnableConnector(Runnable):
    def __init__(self, runnable_list) -> None:
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data

class NakliStrOutputParser(Runnable):
    def __init__(self) -> None:
        pass
    def invoke(self, input_data):
        return input_data['response']

# Chain of components
llm = NakliLLM()
prompt = NakliPromptTemplate(
    template="Tell me about {topic}",
    input_variables=["topic"]
)
parser = NakliStrOutputParser()

chain = RunnableConnector([prompt, llm, parser])
print(chain.invoke(dict(topic="cricket")))

# Chain of chains
template1 = NakliPromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)
template2 = NakliPromptTemplate(
    template="explain the following joke \n{response}",
    input_variables=["response"]
)
llm = NakliLLM()
parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])

chain3 = RunnableConnector([chain1, chain2])
print(chain3.invoke(dict(topic="cricket")))