from typing import Optional
from langgraph.graph import StateGraph
from pydantic import BaseModel
from retriever import retriever
from agent import llm_chain


class State(BaseModel):
    question: str
    retrieved_docs: Optional[list[str]] = []
    answer: Optional[str] = ""


rag_graph = StateGraph(State)

rag_graph.add_node("retrieve", retriever)
rag_graph.add_node("generate", llm_chain)

rag_graph.set_entry_point("retrieve")
rag_graph.add_edge("retrieve", "generate")

graph = rag_graph.compile()