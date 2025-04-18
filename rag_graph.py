from typing import Optional
from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from retriever import retriever
from chatbot import llm_chain
from tools import math_tool
from routers import is_math_question

class State(BaseModel):
    question: str
    retrieved_docs: Optional[list[str]] = []
    answer: Optional[str] = ""
    next_node: Optional[str] = None

rag_graph = StateGraph(State)

rag_graph.add_node("router", lambda state: state)
rag_graph.add_node("retrieve", retriever)
rag_graph.add_node("llm_chain", llm_chain)
rag_graph.add_node("math_tool", math_tool)

rag_graph.set_entry_point("router")
rag_graph.add_conditional_edges(
    "router",
    is_math_question
)
rag_graph.add_edge("retrieve", "llm_chain")
rag_graph.add_edge("math_tool", END)
rag_graph.add_edge("llm_chain", END)

graph = rag_graph.compile()