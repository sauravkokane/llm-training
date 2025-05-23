from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal
load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')


# define schema
json_schema = {
	"title": "Review",
	"type": "object",
	"properties": {
		"key_themes": {
			# for list we are using type array
			"type": "array",
			"items": {
				"type": "string"
			},
			"description": "Write down all the key themes discussed in the review in a list"
		},
		"summary": {
			"type": "string",
			"description": "A brief summary of the review"
		},
		"sentiment": {
			"type": "string",
			# rather than using literal we use enum here.
			"enum": ["pos", "neg"],
			"description": "Return sentiment of the review either negative, positive or neutral"
		},
		"pros": {
			# if a attribute supports multiple types then they should come in array.
			# if any field is optional it will have one of the type as null
			"type": ["array", "null"],
			"items": {
				"type": "string"
			},
			"description": "Write down all the pros inside a list"
		},
		"cons": {
			"type": ["array", "null"],
			"items": {
				"type": "string"
			},
			"description": "Write down all the cons inside a list"
		},
		"name": {
			"type": ["string", "null"],
			"description": "Write the name of the reviewer"
		}
	},
	"required": ["key_themes", "summary", "sentiment"]
}

# Create model with structured output
structured_model = model.with_structured_output(json_schema)

# normal way of invoking

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
"""
)



print(result)

print(type(result))
print(result["name"])



# Output:
# {
# 	'name': 'Saurav Kokane' / 'Anonymous',
# 	'summary': 'The Samsung Galaxy S24 Ultra is an impressive phone boasting a powerful Snapdragon 8 Gen 3 processor, excellent battery life, and a standout 200MP camera, though its weight and pre-installed bloatware are drawbacks.',
# 	'sentiment': 'pos',
# 	'pros': [
# 		'Insanely powerful processor (great for gaming and productivity)', 
# 		'Stunning 200MP camera with incredible zoom capabilities', 
# 		'Long battery life with fast charging', 
# 		'S-Pen support is unique and useful'
# 	],
# 	'cons': [
# 		'Heavy and large, uncomfortable for one-handed use',
# 		'Bloatware from Samsung apps existing alongside Google services',
# 		'High price tag of $1,300'
# 	],
# 	'key_themes': [
# 		'Performance',
# 		'Camera Quality',
# 		'Battery Life',
# 		'Ergonomics',
# 		'Software Experience'
# 	]
# }
# <class 'dict'>
# Saurav Kokane / Anonymous
