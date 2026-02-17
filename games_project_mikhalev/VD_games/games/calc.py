"""Calculator game module."""

import operator
import random

DESCRIPTION = "What is the result of the expression?"


def generate_round():
    """Generate question and answer for calculator game."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    operations = [
        ("+", operator.add),
        ("-", operator.sub),
        ("*", operator.mul),
    ]
    
    op_symbol, op_func = random.choice(operations)
    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(op_func(num1, num2))
    
    return question, correct_answer
