import pytest

import tests
from package.challenge import is_fizzbuzz

tests.__file__


class TestFizzBuzz:
    @pytest.mark.parametrize(
        "number, res",
        [
            (1, "1"),
            (2, "2"),
            (3, "fizz"),
            (5, "buzz"),
            (15, "fizzbuzz"),
        ],
    )
    def test_is_fizzbuzz_return_string_number(self, number: int, res: str):
        assert is_fizzbuzz(number) == res
