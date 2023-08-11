from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

template = "Can you tell me a riddle about {object} with its answer?"

prompt = PromptTemplate(template=template, input_variables=["object"])


prompt = prompt.format(object="ice")
# The "query"
print(prompt)


llm = OpenAI()
# The "response"
print(llm(prompt))
