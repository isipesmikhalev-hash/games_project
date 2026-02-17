"""Calculator game script."""

from ..engine import play_game
from ..games import calc


def main():
    """Run calculator game."""
    play_game(calc)


if __name__ == "__main__":
    main()
