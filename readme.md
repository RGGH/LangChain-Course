# LangChain Course

### Introduction ~ LangChain : what is it, how does it work, why might you use it?
<div>
<a href="https://www.youtube.com/watch?v=jfJbaJHnnP0">
    <img src="https://github.com/RGGH/LangChain-Course/blob/main/readme/thumb1.jpg" alt="Python360 YouTube" width="200"/>
</a><br>
</div>
<br/><br/>
“First, **it makes it easier to build applications that use LLMs**. LLMs are complex models that can be difficult to use directly. LangChain provides a simple interface that makes it easy to connect LLMs to your application. Second, LangChain allows you to connect LLMs to other sources of data.

### TLDR;

**Components - prompt templates**

**Chains - solve a specific task**

**Agents - allow LLMs to interact (with external APIs)**

### Without LangChain vs with LangChain

Available for **Python *and* JavaScript**

[https://js.langchain.com/docs/get_started/introduction/](https://js.langchain.com/docs/get_started/introduction/)

[https://python.langchain.com/docs/get_started/introduction.html](https://python.langchain.com/docs/get_started/introduction.html)

If you want to create a GUI then try “Streamlit” in Python, or sign up for [https://www.langflow.org/](https://www.langflow.org/) or try [https://flowiseai.com/](https://flowiseai.com/)

Features of LangChain:

- Models
- Prompts
- Chains
- Memory
- Indexes
- Agents & Tools

**Use Cases:**

- [Chatbots](https://python.langchain.com/docs/use_cases/chatbots/)
- [Answering questions using sources](https://python.langchain.com/docs/use_cases/question_answering/)
- [Analyzing structured data](https://python.langchain.com/docs/use_cases/tabular.html)

### 1 - Try **the OpenAI API *without* LangChain**

[https://platform.openai.com/examples](https://platform.openai.com/examples)

[https://platform.openai.com/playground](https://platform.openai.com/playground)

- Go to [http://platform.openai.com](http://platform.openai.com/)
- Sign in, and start testing prompts!
- Save your API key in .env file or ~/.zshrc !

```jsx
export OPENAI_API_KEY=sk-xsssdfsddf67sadfasdfOXT3BlbkFJo12Ssdafdfasfadsfsafas
```

- Add .env to gitignore
- I use a global gitignore file

```jsx
pip install openai
```

****ChatGPT API Transition Guide :****

'role' can take one of three values:

'system',

'user'

'assistant’

Sign up to OpenAI if do you want to use them with your projects - requires credit card*

### Tips to save $

Use caching + FakeLLM

Set a billing limit

View token usage in your code :

You can try free LLMs but they often need RAM == $$$

![Untitled](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/Untitled%201.png)

```bash
from langchain.callbacks import get_openai_callback
```

---

### **2 - Install LangChain**

Install LangChain:

```jsx
pip install langchain
```

LangChain automates LLM calls, choose whichever LLM you prefer

[https://python.langchain.com/docs/integrations/llms/openai](https://python.langchain.com/docs/integrations/llms/openai)

---

### 3 - **Models**

There are lots of LLM providers (OpenAI, Cohere, Hugging Face, etc) - the `LLM` class is designed to provide a standard interface for all of them.

[https://python.langchain.com/docs/use_cases/chatbots/#overview](https://python.langchain.com/docs/use_cases/chatbots/#overview)

You can use `LLMs` (see [here](https://python.langchain.com/docs/modules/model_io/models/llms)) for chatbots as well, but chat models have a more conversational tone and natively support a message interface.

```jsx
from langchain.llms import OpenAI
from langchain.llms import Cohere
from langchain.llms import GooseAI
```

Once you have imported you can create an instance of it

```python
llm = OpenAI()
```

As of August 2023 - **gpt-3.5-turbo is the default model for the OpenAI class if you don’t specify anything inside the brackets.**

What is the difference between LLM and chat model in LangChain?

- [LLMs](https://python.langchain.com/docs/modules/model_io/models/llms/): Models that take a text string as input and return a text string
- [Chat models](https://python.langchain.com/docs/modules/model_io/models/chat/): Models that are backed by a language model but take a list of Chat Messages as input and return a Chat Message

Chat Models: **Unlike LLMs, chat models take chat messages as inputs and return them as outputs**.

[https://platform.openai.com/docs/guides/gpt/which-model-should-i-use](https://platform.openai.com/docs/guides/gpt/which-model-should-i-use)

**`gpt-3.5-turbo`** returns outputs with lower latency and costs much less per token

![Untitled](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/Untitled%202.png)

.predict and .run methods are usually the same!

### 4 - Prompts

TLDR; “Prompts are the text that you send to the LLM”

[https://python.langchain.com/docs/modules/model_io/prompts/](https://python.langchain.com/docs/modules/model_io/prompts/)

A prompt for a language model is a **set of instructions or input provided by a user** to guide the model's response, helping it understand the context and generate relevant and coherent language-based output, such as answering questions, completing sentences, or engaging in a conversation.

It’s like a Python f-string…Use a prompt template and you can pass a dynamically formed question.

```jsx
from langchain import PromptTemplate
```

ChatPromptTemplate

PromptTemplate

[https://learnprompting.org/docs/category/-basics](https://learnprompting.org/docs/category/-basics)

[https://platform.openai.com/playground](https://platform.openai.com/playground)

Single shot v Few Shot

[https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/few_shot_examples](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/few_shot_examples)

[https://platform.openai.com/docs/guides/gpt/chat-completions-vs-completions](https://platform.openai.com/docs/guides/gpt/chat-completions-vs-completions)

Prompts, Chains and Parser Basics

### 5 - Chains

SimpleSequentialChain - produces only 1 output

SequentialChain - output of 1st chain goes into next chain  - *chain takes a dict!

```jsx
from langchain.chains import ...
```

### 6 - Router Chains

The RouterChain itself (responsible for selecting the next chain to call)

Use `MultiPromptChain` to create a question-answering chain that selects the prompt which is most relevant for a given question. e.g. physics_template and maths_template

### 7 - Memory

**By default, LLMs are stateless,** which means each incoming query is processed independently of other interactions without memory, so every query is treated as an entirely independent input without considering past interactions.

**Memory - Buffer vs. Summary**

```jsx
from langchain.memory import ChatMessageHistory
```

```bash
# Retrieve chat messages with ConversationBufferHistory (as a variable)
from langchain.memory import ConversationBufferMemory
```

ConversationBufferMemory stores everything, but uses lots of tokens and response is slower.

```bash
from langchain.memory import ConversationBufferMemory
# useful for keeping a sliding window of the most recent interactions, 
# so the buffer does not get too large
```

```bash
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
```

ConversationSummaryMemory keeps a **summarized** form of the conversation.

> “Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.”

```bash
conversation_sum = ConversationChain(
    llm=llm, 
    memory=ConversationSummaryMemory(llm=llm)
)
```

```bash
# extracts information on entities (using an LLM) and 
# builds up its knowledge about that entity over time (also using an LLM)
from langchain.memory import ConversationEntityMemory
```

**More memory options:**

```bash
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)
```

[https://python.langchain.com/docs/modules/memory/#using-a-chatmodel](https://python.langchain.com/docs/modules/memory/#using-a-chatmodel)

[https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/](https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/)

### [View the Memory Store](https://python.langchain.com/docs/modules/memory/types/entity_summary_memory#inspecting-the-memory-store)

```bash
from pprint import pprint
pprint(conversation.memory.entity_store.store)
```

### Indexes

- Document loaders
- Text splitters
- Retrievers
- Vector stores - embed text as vectors (Similarity Search)

![qdrant_langchain_FAISS_v_LLM-1024x502.png](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/qdrant_langchain_FAISS_v_LLM-1024x502.png)

[https://www.pinecone.io/](https://www.pinecone.io/)

[https://qdrant.tech/](https://qdrant.tech/)

[https://python.langchain.com/docs/integrations/vectorstores/qdrant](https://python.langchain.com/docs/integrations/vectorstores/qdrant)

[https://python.langchain.com/docs/use_cases/question_answering/](https://python.langchain.com/docs/use_cases/question_answering/)

[https://redandgreen.co.uk/text-embedding-and-upsert-with-qdrant-in-python/ai-ml/](https://redandgreen.co.uk/text-embedding-and-upsert-with-qdrant-in-python/ai-ml/)

```python
pip install langchain.vectorstores langchain.embeddings 
langchain.text_splitter qdrant_client numpy sentence_transformers tqdm
```

![al1.png](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/al1.png)

```python
import langchain
langchain.debug = True
```

```jsx
python3.10 -i q1.py
```

![Untitled](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/Untitled%203.png)

![Screenshot from 2023-08-15 10-11-31.png](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/Screenshot_from_2023-08-15_10-11-31.png)

### Agents - LLMs plus Tools

Language models can run Python code! - tool = PythonREPL()

How ChatGPT Plugins work

Evaluation - Use LLMs to evaluate LLMs

### Links

[https://github.com/kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain)

[https://github.com/openai/openai-cookbook](https://github.com/openai/openai-cookbook)

[https://platform.openai.com/](https://platform.openai.com/)

[https://alphasec.io/langchain-decoded-part-1-models/](https://alphasec.io/langchain-decoded-part-1-models/)

[https://platform.openai.com/playground](https://platform.openai.com/playground)

[https://github.com/pinecone-io/examples/tree/master/learn/generation/langchain/handbook](https://github.com/pinecone-io/examples/tree/master/learn/generation/langchain/handbook)

Watch the video :

![LangChain_Full_COurse.png](LangChain%20Course%2073d458248b16461a98caa17452fe82fa/LangChain_Full_COurse.png)
