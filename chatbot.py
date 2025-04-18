from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="llama3", temperature=0)

prompt = PromptTemplate(
    template=""""
    You are a helpful assistant. Use the context to answer the question.
    You must not answer or give suggestions if the question is not realated to the context. 
    If the question is not related you can simply answer: Sorry, this question is not related to the current knowledge base. Therefore, I'm not allowed to answer it.
    
    
    Context:
    {context}

    Question:
    {question}

    Answer:
    """,
    input_variables=["question", "context"],
)

def llm_chain(state):
    print("Interacting with LLM model...")
    question = state.question
    docs = state.retrieved_docs
    context = "\n".join(docs)
    formatted_prompt = prompt.format(question=question, context=context)
    answer = llm.invoke(formatted_prompt)
    state.answer = answer.content
    return state