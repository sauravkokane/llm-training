from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
code = """
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # Instance variable
        self.model = model      # Instance variable
        self.year = year        # Instance variable
        self.engine_on = False  # Another variable to track state

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"The {self.brand} {self.model}'s engine is now ON.")
        else:
            print(f"The engine is already running.")

    def get_info(self):
        return f"Car Info: {self.year} {self.brand} {self.model}"

# Creating an object of Car class
my_car = Car("Toyota", "Corolla", 2022)

# Calling methods on the object
print(my_car.get_info())    # Outputs car information
my_car.start_engine()       # Starts the engine
my_car.start_engine()       # Trying to start again (should warn)

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=650,
    chunk_overlap=0,
)

result = splitter.split_text(code)

print(len(result))

for i, r in enumerate(result):
    print([i], len(r), r)