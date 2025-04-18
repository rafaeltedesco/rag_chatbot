from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

TRANSFORMER_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(TRANSFORMER_NAME)

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="rag_docs",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(TRANSFORMER_NAME)
)

def add_documents(docs):
    print("Loading documents as embeddings...")
    for idx, doc in enumerate(docs):
        collection.add(documents=[doc], ids=[f"doc_{idx}"])
        

def retrieve(question: str, k=3):
    print("Retrieving documents for question...")
    results = collection.query(query_texts=[question], n_results=k)
    documents = results["documents"][0]
    print(f"{len(documents)} documents found...")
    return results["documents"][0]

def retriever(state):
    question = state.question
    docs = retrieve(question)
    state.retrieved_docs = docs
    return state