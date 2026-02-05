
from __future__ import annotations

Number = int | float

def soma(a: Number, b: Number) -> Number:
    return a + b

def sub(a: Number, b: Number) -> Number:
    return a - b

def mult(a: Number, b: Number) -> Number:
    return a * b

def div(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Não dá pra dividir por zero.\n Tente novamente!")
    return a / b