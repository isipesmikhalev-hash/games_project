"""Game engine for brain games."""

from .cli import welcome_user


def play_game(game_module) -> None:
    """Run the game engine.

    Args:
        game_module: Module with game logic containing
                    DESCRIPTION and generate_round() function

    """
    name = welcome_user()
    print(game_module.DESCRIPTION)
    
    rounds_count = 0
    while rounds_count < 3:
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
            rounds_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
