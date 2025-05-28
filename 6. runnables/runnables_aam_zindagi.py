import random

class NakliLLM:
    def __init__(self) -> None:
        print("LLM created")

    def predict(self, prompt):
        response_list = [
            "Prague is very good city.",
            "Virat Kohli is a cricket player",
            "Mumbai is famous for its street food"
        ]
        return {'response': random.choice(response_list)}

llm = NakliLLM()
llm.predict("tell me about Mumbai")

class NakliPromptTemplate:
    def __init__(self, template, input_variables=[], partial_variables={}):
        self.template = template
        self.input_variables = input_variables
        self.partial_variables = partial_variables
    def format(self, input_dict):
        input_dict.update(self.partial_variables)
        print(input_dict)
        return self.template.format(**input_dict)
    def __str__(self):
        return self.template

template = NakliPromptTemplate(
    template="Write a {length} poem about a {topic}",
    input_variables=['topic', 'length']
)
prompt = template.format(dict(topic="India", length="short"))
print(llm.predict(prompt))

class NakliLLMChain:
    def __init__(self, llm, prompt) -> None:
        self.llm = llm
        self.prompt = prompt
    def run(self, input_dict):
        prompt_value = self.prompt.format(input_dict)
        print(prompt_value)
        return self.llm.predict(prompt_value)

llm = NakliLLM()
template = NakliPromptTemplate(
    template="Write a {length} poem about a {topic}",
    input_variables=['topic', 'length']
)
chain = NakliLLMChain(llm, template)
chain.run({'topic': 'dog', 'length': 'long'})