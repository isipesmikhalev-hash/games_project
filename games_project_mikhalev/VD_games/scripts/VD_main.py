"""VD main module."""

from ..cli import welcome_user


def main() -> None:
    """Run the main game."""
    print("Welcome to the Brain Games!")
    welcome_user()


if __name__ == "__main__":
    main()
