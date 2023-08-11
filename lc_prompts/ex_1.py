from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

template = "Can you tell me a riddle about {object} with its answer?"

prompt = PromptTemplate(template=template, input_variables=["object"])


prompt = prompt.format(object="ice")

# The "query" - you can print this to check it without using any tokens!
print(prompt)


llm = OpenAI()
# The "response"
print(llm(prompt))
