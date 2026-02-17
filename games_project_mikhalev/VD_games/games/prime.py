"""Prime number game module."""

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check if number is prime."""
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def generate_round():
    """Generate question and answer for prime game."""
    number = random.randint(1, 50)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return question, correct_answer
