import random
from unittest.mock import patch

import pytest

from src.guess_number import guess_number, random_number


@patch("random.randint")
def test_random_number(mock_rand):
    mock_rand.return_value = 1234
    result = random_number()
    assert result == 1234


@pytest.mark.parametrize("number, input_num, result",
                         [(1234, "1234", (['1', '2', '3', '4'], [])), (1234, "1432", (['1', '3'], ['2', '4'])),
                          (1234, "5678", ([], [])), (1234, "4321", ([], ['1', '2', '3', '4'])),
                          (1111, "1432", (['1'], ['1', '1', '1'])), (1234, "1546", (['1'], ['4']))])
def test_guess_number(number, input_num, result):
    assert guess_number(number, input_num) == result
