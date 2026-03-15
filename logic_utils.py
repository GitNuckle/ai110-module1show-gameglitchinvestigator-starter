def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret) -> str:
    """
    Compares the guess with the secret number and returns the outcome.

    Args:
        guess (int): The guessed number.
        secret (int or str): The secret number to compare against.

    Returns:
        str: The outcome — "Win", "Too High", or "Too Low".
    """
    if guess == secret:
        return "Win"

    try:
        return "Too High" if guess > secret else "Too Low"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win"
        return "Too High" if g > secret else "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
