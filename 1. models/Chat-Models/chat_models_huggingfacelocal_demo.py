from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_home'

# Ensure the model_id is specified when creating HuggingFacePipeline
hf = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-1b-it",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100},
)

chat = ChatHuggingFace(llm=hf, model_id="Qwen/Qwen3-0.6B", verbose=True) # <-- Added model_id here
result = chat.invoke("What is capital of India?")
print(result.content)