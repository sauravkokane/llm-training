from huggingface_hub import login
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

login(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

repo_id = "meta-llama/Llama-3.2-3B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task = 'text-generation',
    max_length=128,
    temperature=0.5,
)

model = ChatHuggingFace(llm=llm)


# 1st prompt -> detailed report
template1 = PromptTemplate(
	template="Write a detailed report on {topic}",
	input_variables=['topic']
)


# 2nd prompt -> summary
template2 = PromptTemplate(
	template="Write a pipeline summary on following text: \n{text}",
	input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser


result = chain.invoke({'topic': "black holes"})


print(result)

# Output:
# **Pipeline Summary: Black Holes**

# **Introduction**

# The pipeline summary provides an overview of the comprehensive report on black holes, covering their formation, properties, types, and the latest research on these enigmatic objects.

# **Key Findings**

# 1. **Formation of Black Holes**: Black holes are formed when a massive star collapses in on itself, causing a massive amount of matter to be compressed into an incredibly small space.
# 2. **Properties of Black Holes**: Black holes have several properties, including an event horizon, singularity, gravitational field, and Hawking radiation.
# 3. **Types of Black Holes**: There are four types of black holes, including stellar, supermassive, intermediate-mass, and primordial black holes.
# 4. **Observational Evidence**: Black holes can be inferred by observing the effects they have on the surrounding environment, including X-rays, gamma rays, radio waves, gravitational waves, and star motions.
# 5. **Latest Research**: Recent research has led to exciting discoveries, including the first image of a black hole, detection of gravitational waves, and insights into Hawking radiation and black hole mergers.

# **Methodology**

# The report uses a comprehensive approach, covering the formation, properties, types, and observational evidence for black holes. The latest research is also discussed, highlighting the latest discoveries and advancements in the field.

# **Data Sources**

# The report cites several references, including scientific papers and publications, to support the findings and provide a comprehensive understanding of black holes.

# **Recommendations**

# The report provides recommendations for future research, including imaging black holes, gravitational wave astronomy, Hawking radiation, and black hole mergers.

# **Conclusion**

# The pipeline summary provides a comprehensive overview of black holes, covering their formation, properties, types, and the latest research on these enigmatic objects. The report highlights the importance of ongoing research and observations to gain a deeper understanding of black holes and their role in the universe.

# **Pipeline Metrics**

# 1. **Data Quality**: The report provides high-quality data on black holes, including their formation, properties, and types.
# 2. **Methodological Rigor**: The report uses a comprehensive approach, covering multiple aspects of black holes, and cites several references to support the findings.
# 3. **Research Impact**: The report highlights the latest discoveries and advancements in the field, demonstrating the impact of ongoing research on our understanding of black holes.
# 4. **Recommendations**: The report provides actionable recommendations for future research, demonstrating the potential for continued progress in the field.
