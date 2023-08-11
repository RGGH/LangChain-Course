from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)

# initialize chat model
chat = ChatOpenAI(temperature=0)
user_input = input("Ask a question")

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content=user_input)
]

print(chat(messages))
