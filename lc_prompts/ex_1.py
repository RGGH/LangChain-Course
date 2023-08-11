from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


template = "Can you tell me a riddle about {topic} with your answer?"

prompt = PromptTemplate(template=template, input_variables=["topic"])


prompt = prompt.format(topic="flowers")

# The "query" - you can print this to check it without using any tokens!
print(prompt)


llm = OpenAI()
# The "response"
print(llm(prompt))
