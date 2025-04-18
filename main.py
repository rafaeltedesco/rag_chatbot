import json
from retriever import add_documents
from rag_graph import graph as chatbot, State

with open("data/docs.json") as f:
    docs = json.load(f)

add_documents(docs)

while True:
    question = input("Enter you question here: ")

    if question == "bye":
        print("See you later!")
        break

    initial_state = State(question=question)

    result = chatbot.invoke(initial_state)

    print("Answer:\n", result["answer"])
    