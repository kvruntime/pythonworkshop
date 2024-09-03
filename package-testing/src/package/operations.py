# coding:utf-8
def add(a: int, b: int) -> int:
    return a + b


def div(a: int, b: int) -> float:
    if a <= 0:
        raise ZeroDivisionError
    return a / b
