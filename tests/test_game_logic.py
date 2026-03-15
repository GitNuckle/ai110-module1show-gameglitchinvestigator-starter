import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_direction_bug():
    # Regression: secret=63, guess=50 — guess is lower than secret,
    # so outcome must be "Too Low" (not "Too High").
    # Previously the outcomes were swapped, causing the wrong hint direction.
    result = check_guess(50, 63)
    assert result == "Too Low", "Guess below secret should return 'Too Low', not 'Too High'"

    result = check_guess(80, 63)
    assert result == "Too High", "Guess above secret should return 'Too High', not 'Too Low'"
