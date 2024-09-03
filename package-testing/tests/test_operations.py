import pytest

from package.operations import add, div


class TestOperationAddInputs:
    @pytest.mark.parametrize(
        "a,b,r",
        [
            (1, 2, 3),
            (1, 4, 5),
        ],
    )
    def test_operation_with_correct_value(self, a, b, r):
        assert add(a, b) == r


class TestOperationDivide:
    def test_divide_with_0_raise_zero_division_error(self):
        with pytest.raises(ZeroDivisionError):
            div(1, 0)

    def test_divide_with_correct_produce_results(self):
        assert div(1, 1) == 1
        return None
