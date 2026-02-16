"""VD games main module."""

from VD_games.cli import welcome_user


def main() -> None:
    """Run the brain games."""
    print("Welcome to the Brain Games!")
    welcome_user()


if __name__ == "__main__":
    main()
