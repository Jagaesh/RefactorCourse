import pytest
import guess_game

def test_input_correct():
    assert guess_game.run_guess(5, 5) is True

def test_input_wrong_guess():
    assert guess_game.run_guess(3, 5) is False

def test_input_wrong_number():
    assert guess_game.run_guess(11, 5) is None

def test_input_wrong_type():
    with pytest.raises(ValueError):
        guess_game.run_guess('abc', 5)

def test_input_wrong_type_2():
    with pytest.raises(ValueError):
        guess_game.run_guess('3', 5)

def test_input_wrong_type_3():
    with pytest.raises(ValueError):
        guess_game.run_guess('0', 5)

def test_input_wrong_type_4():
    with pytest.raises(ValueError):
        guess_game.run_guess('5', 5)


if __name__ == "__main__":
    pytest.main([__file__])
