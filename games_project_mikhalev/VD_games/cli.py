"""CLI module for user interaction."""

import prompt


def welcome_user() -> None:
    """Welcome user by asking their name."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
