"""Arithmetic progression game module."""

import random

DESCRIPTION = "What number is missing in the progression?"


def generate_progression() -> tuple[list, int]:
    """Generate arithmetic progression and index of hidden element."""
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    
    return progression, hidden_index


def generate_round():
    """Generate question and answer for progression game."""
    progression, hidden_index = generate_progression()
    
    # Создаем вопрос со скрытым элементом
    progression_with_hidden = progression.copy()
    progression_with_hidden[hidden_index] = ".."
    
    question = " ".join(str(x) for x in progression_with_hidden)
    correct_answer = str(progression[hidden_index])
    
    return question, correct_answer
