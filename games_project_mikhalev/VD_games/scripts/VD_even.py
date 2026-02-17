"""Even number check game."""

import random

from ..cli import welcome_user


def is_even(number: int) -> bool:
    """Check if number is even."""
    return number % 2 == 0


def play_round() -> bool:
    """Play one round of the game. Return True if player correct."""
    number = random.randint(1, 100)
    print(f"Question: {number}")
    
    answer = input("Your answer: ").strip().lower()
    correct_answer = "yes" if is_even(number) else "no"
    
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


def main() -> None:
    """Run the even number game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    while correct_answers < 3:
        if play_round():
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
