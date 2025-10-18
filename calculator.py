from typing import Union

Numeric = Union[int, float]


def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b


def subtract(a: Numeric, b: Numeric) -> Numeric:
    return a - b


def multiply(a: Numeric, b: Numeric) -> Numeric:
    return a * b


def divide(a: Numeric, b: Numeric) -> float:
    return a / b
