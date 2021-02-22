def calculate(n: int) -> int:
    if n < 0:
        raise ValueError("n should be a positive integer")

    if n == 0 or n == 1:
        return n

    return calculate(n - 1) + calculate(n - 2)
