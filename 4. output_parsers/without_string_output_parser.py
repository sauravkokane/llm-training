from huggingface_hub import login
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
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


prompt1 = template1.invoke({'topic': "black hole"})

detailed_report = model.invoke(prompt1)


prompt2 = template2.invoke({'text': detailed_report.content})


summary = model.invoke(prompt2)


print(detailed_report)
print(summary.content)



# "**Black Hole Report**
# **Introduction**
# A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape. It is formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime around it. Black holes are among the most mysterious and fascinating objects in the universe, and scientists have been studying them for decades to learn more about their properties and behavior.
# **Formation of a Black Hole**
# The formation of a black hole typically occurs when a massive star runs out of fuel and dies. The star collapses under its own gravity, causing a massive amount of matter to be compressed into an incredibly small space. This compression creates an intense gravitational field that warps the fabric of spacetime around the star, creating a boundary called the event horizon.
# The event horizon is the point of no return around a black hole. Any matter or radiation that crosses the event horizon is trapped by the black hole's gravity and cannot escape. The point of no return is determined by the mass of the black hole and the speed of the object approaching it.
# **Types of Black Holes**
# There are four types of black holes, each with different properties and origins:
# 1. **Stellar Black Holes**: These are the smallest and most common type of black hole, formed from the collapse of individual stars.\n2. **Supermassive Black Holes**: These are the largest type of black hole, found at the centers of galaxies and with masses millions or even billions of times that of the sun.\n3. **Intermediate-Mass Black Holes**: These black holes have masses that fall between those of stellar and supermassive black holes.\n4. **Primordial Black Holes**: These are hypothetical black holes that may have formed in the early universe before the first stars formed.
# **Properties of Black Holes**
# Black holes have several properties that make them fascinating objects of study:
# 1. **Mass**: The mass of a black hole determines the strength of its gravitational field and the size of its event horizon.\n2. **Spin**: The spin of a black hole affects its rotation and the way it warps spacetime around it.\n3. **Charge**: The charge of a black hole affects its interaction with other charged objects and the way it warps spacetime around it.\n4. **Temperature**: The temperature of a black hole is related to its entropy and the way it radiates energy.
# **Observational Evidence for Black Holes**
# While black holes themselves are invisible, their presence can be inferred from the effects they have on the surrounding environment. Some of the observational evidence for black holes includes:
# 1. **X-rays and Gamma Rays**: Telescopes can detect X-rays and gamma rays emitted by hot gas swirling around black holes.\n2. **Radio Waves**: Radio telescopes can detect radio waves emitted by matter as it spirals into a black hole.\n3. **Gravitational Waves**: The detection of gravitational waves by LIGO and VIRGO provide strong evidence for the existence of black holes.\n4. **Star Motions**: Astronomers can observe the motions of stars near a suspected black hole to determine if they are being affected by its gravity.
# **The Information Paradox**
# One of the most puzzling aspects of black holes is the information paradox. According to quantum mechanics, information cannot be destroyed, but the laws of general relativity suggest that anything that falls into a black hole is lost forever. This paradox has led to a lot of debate and research in the field of theoretical physics.
# **The Role of Black Holes in the Universe**
# Black holes play a crucial role in the universe, particularly in the formation and evolution of galaxies. Some of the ways black holes affect the universe include:
# 1. **Galaxy Formation**: Supermassive black holes are thought to have played a key role in the formation and evolution of galaxies.\n2. **Star Formation**: The presence of a black hole can affect the formation of stars in a galaxy.\n3. **Cosmic Evolution**: Black holes can affect the large-scale structure of the universe, particularly in the distribution of galaxies and galaxy clusters.
# **Conclusion**
# Black holes are fascinating objects that continue to capture the imagination of scientists and the public alike. While we have made significant progress in understanding black holes, there is still much to be learned about these mysterious objects. Further research is needed to resolve the information paradox and to better understand the role of black holes in the universe.
# **Recommendations for Future Research**
# 1. **Direct Detection of Black Holes**: Developing new technologies to directly detect black holes would be a major breakthrough in the field.\n2. **Theoretical Models**: Developing new theoretical models that can explain the behavior of black holes would be essential for resolving the information paradox.\n3. **Observational Studies**: Conducting observational studies of black holes would provide valuable insights into their properties and behavior.\n4. **Simulations**: Developing simulations of black hole formation and evolution would help us better understand the role of black holes in the universe.
# **References**
# 1. Hawking, S. W. (1974). Black hole explosions? Nature, 248(5443), 30-31.\n2. Penrose, R. (1969). Gravitational collapse and space-time singularities. Physical Review Letters, 23(17), 1024-1027.\n3. Thorne, K. S. (1974). Black holes and time machines. In Black Holes (pp. 231-244).\n4. Rees, M. J. (1997). Black holes, neutron stars, and cosmology. Cambridge University Press.
# Note: This report is a general overview of black holes and is not intended to be a comprehensive or definitive treatment of the subject." additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 1175, 'prompt_tokens': 42, 'total_tokens': 1217}, 'model_name': 'meta-llama/Llama-3.2-3B-Instruct', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run--263922e8-f4c5-4739-b9ad-0a5de5267e11-0' usage_metadata={'input_tokens': 42, 'output_tokens': 1175, 'total_tokens': 1217}
# **Pipeline Summary: Black Holes**

# **I. Introduction**

# * Black holes are regions in space with such strong gravitational pull that nothing, including light, can escape.
# * Formed when a massive star collapses, creating an intense gravitational field that warps spacetime.

# **II. Formation and Types of Black Holes**

# * Formation: Collapse of massive stars, compression of matter, and creation of event horizon.
# * Types:
# 	1. Stellar Black Holes: Smallest and most common, formed from individual star collapse.
# 	2. Supermassive Black Holes: Largest, found at galaxy centers, with masses millions or billions of solar masses.
# 	3. Intermediate-Mass Black Holes: Masses between stellar and supermassive black holes.
# 	4. Primordial Black Holes: Hypothetical, formed in early universe before first stars.

# **III. Properties of Black Holes**

# * Mass: Determines gravitational field strength and event horizon size.
# * Spin: Affects rotation and spacetime warping.
# * Charge: Affects interaction with charged objects and spacetime warping.
# * Temperature: Related to entropy and energy radiation.

# **IV. Observational Evidence**

# * X-rays and Gamma Rays: Telescopes detect hot gas swirling around black holes.
# * Radio Waves: Radio telescopes detect matter spiraling into black holes.
# * Gravitational Waves: LIGO and VIRGO detection provides strong evidence for black holes.
# * Star Motions: Astronomers observe star motions near suspected black holes.

# **V. The Information Paradox**

# * Quantum mechanics suggests information cannot be destroyed, but general relativity implies anything falling into a black hole is lost.
# * Debate and research continue to resolve this paradox.

# **VI. The Role of Black Holes in the Universe**

# * Galaxy Formation: Supermassive black holes played key role in galaxy evolution.
# * Star Formation: Black holes affect star formation in galaxies.
# * Cosmic Evolution: Black holes influence large-scale structure of the universe.

# **VII. Conclusion**

# * Black holes continue to fascinate scientists and the public.
# * Further research is needed to resolve the information paradox and understand black holes' role in the universe.

# **VIII. Recommendations for Future Research**

# * Direct detection of black holes
# * Theoretical models to explain black hole behavior
# * Observational studies of black holes
# * Simulations of black hole formation and evolution