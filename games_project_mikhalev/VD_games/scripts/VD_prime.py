"""Prime number game script."""

from ..engine import play_game
from ..games import prime


def main():
    """Run prime number game."""
    play_game(prime)


if __name__ == "__main__":
    main()
