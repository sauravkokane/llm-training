import re
research_papers_list = [
    "Computing Machinery and Intelligence",
    "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain",
    "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence",
    "Learning Representations by Back-Propagating Errors",
    "Long Short-Term Memory",
    "ImageNet Classification with Deep Convolutional Neural Networks",
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "Language Models are Few-Shot Learners",
    "Deep Residual Learning for Image Recognition"
]

# [
#     "Mixtral of Experts",
#     "Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model",
#     "Genie: Generative Interactive Environments",
#     "DoRA: Weight-Decomposed Low-Rank Adaptation",
#     "Gemma: Open Models Based on Gemini Research and Technology",
#     "KAN: Kolmogorov-Arnold Networks",
#     "Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3",
#     "The Llama 3 Herd of Models",
#     "Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone",
#     "Movie Gen: A Cast of Media Foundation Models"
# ]

input_styles = [
    "Beginner-Friendly", 
    "Technical", 
    "Code-Oriented", 
    "Mathematical"
]

input_lengths = [
    "Short (1-2 paragraphs)", 
    "Moderate (3-5) paragraphs", 
    'Long (detailed explanation)'
]



def render_latex(ip_str):
    # Convert to proper LaTeX format
    latex_str = (
        ip_str
        .replace("sigmoid", r"\sigma")  # Replace function names
        .replace("tanh", r"\tanh")
        .replace("*", "")  # Remove asterisks (LaTeX uses implicit multiplication)
    )
    
    # Fix subscripts (convert h_(t-1) to h_{t-1})
    latex_str = re.sub(r'(\w+)_\(([^)]+)\)', r'\1_{\2}', latex_str)
    
    # Wrap in math mode
    return f"$${latex_str}$$"