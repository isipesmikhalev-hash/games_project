"""GCD game module."""

import random
import math


DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    """Generate question and answer for GCD game."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    
    return question, correct_answer
