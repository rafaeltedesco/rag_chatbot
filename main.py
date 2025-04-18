import json
from retriever import add_documents, retrieve

with open("data/docs.json") as f:
    docs = json.load(f)

add_documents(docs)

documents = retrieve("what is chroma DB?")

print(documents, "docs")