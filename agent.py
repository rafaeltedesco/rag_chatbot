from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable

llm = ChatOllama(model="llama3")

prompt = PromptTemplate(
    template=""""
    You are a helpful assistant. Use the context to answer the question

    Context:
    {context}

    Question:
    {question}

    Answer:
    """,
    input_variables=["question", "context"],
)

def llm_chain(state):
    question = state["question"]
    docs = state["retrieved_docs"]
    context = "\n".join(docs)
    formatted_prompt = prompt.format(question=question, context=context)
    answer = llm.invoke(formatted_prompt)
    state["answer"] = answer
    return state