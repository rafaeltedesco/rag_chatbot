def is_math_question(state):
    question = state.question
    operators = ['+', '-', '/', '*']
    if any(operator in question for operator in operators):
        return "math_tool" 
    return "retrieve"