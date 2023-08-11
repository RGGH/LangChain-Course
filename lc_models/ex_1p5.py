import openai
from langchain.llms import OpenAI


llm = OpenAI()
answer = llm("Why did the chicken cross the road?")
print(answer)
