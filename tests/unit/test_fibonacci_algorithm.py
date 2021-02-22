import pytest

from src.algorithms import fibonacci


def test_negative_n() -> None:
    with pytest.raises(ValueError) as excinfo:
        assert fibonacci.calculate(-1)
    assert "n should be a positive integer" in str(excinfo.value)


@pytest.mark.parametrize("n, expected_result", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
])
def test_fibonacci(n, expected_result) -> None:
    assert fibonacci.calculate(n) == expected_result
