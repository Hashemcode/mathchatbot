import re
import math
import sympy

def evaluate_math_expression(expression):
    # Remove non-alphanumeric characters except for operators and decimal point
    expression = re.sub(r'[^0-9+\-*/.^]', '', expression)

    try:
        # Evaluate the math expression using SymPy library for more advanced math operations
        expr = sympy.sympify(expression)
        result = expr.evalf()
        return result
    except (sympy.SympifyError, ValueError, ZeroDivisionError) as e:
        return None

def simplify_math_expression(expression):
    try:
        # Simplify the math expression using SymPy library
        expr = sympy.sympify(expression)
        simplified_expr = sympy.simplify(expr)
        return str(simplified_expr)
    except (sympy.SympifyError, ValueError) as e:
        return None

# Start the conversation loop
while True:
    user_input = input('You: ')

    # Check if the user input is a math expression
    if re.search(r'[0-9+\-*/.^]+', user_input):
        result = evaluate_math_expression(user_input)

        if result is not None:
            print('ChatBot:', result)
        else:
            simplified_expr = simplify_math_expression(user_input)
            if simplified_expr is not None:
                print('ChatBot: The expression simplifies to:', simplified_expr)
            else:
                print('ChatBot: Sorry, I could not evaluate or simplify the math expression.')
    else:
        print('ChatBot: I am a math chatbot. Please provide a math expression.')
