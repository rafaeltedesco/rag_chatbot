from sympy import sympify
from sympy.core.sympify import SympifyError

def math_tool(state):
    print("Calling math tool...")
    question = state.question
    formula_queue = []
    for char in question:
        if char.isnumeric() or char in ['+', '-', '*', '/']:
            formula_queue.append(char)
    question = ''.join(formula_queue)
    try:
        expr = sympify(question)
        result = expr.evalf()
        state.answer = f"{question} is {result:.2f}"
        return state
    except SympifyError:
        state.answer = "Sorry, I couldn't understand the math expression"
        return state