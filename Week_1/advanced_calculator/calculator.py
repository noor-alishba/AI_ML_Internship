"""
calculator.py

Defines the Calculator class, which encapsulates all arithmetic and
scientific operations, a single memory register, and a running
calculation history for the command-line calculator.
"""

import math

from validator import Validator, ValidationError


class Calculator:
   
    

    def __init__(self):
        self._history = []
        self._memory = 0.0

    # Basic arithmetic operations

    def add(self, first: float, second: float) -> float:
        result = first + second
        self._record_history(f"{first} + {second} = {result}")
        return result

    def subtract(self, first: float, second: float) -> float:
        result = first - second
        self._record_history(f"{first} - {second} = {result}")
        return result

    def multiply(self, first: float, second: float) -> float:
        result = first * second
        self._record_history(f"{first} * {second} = {result}")
        return result

    def divide(self, first: float, second: float) -> float:
        Validator.validate_non_zero(second)
        result = first / second
        self._record_history(f"{first} / {second} = {result}")
        return result

    def modulus(self, first: float, second: float) -> float:
        Validator.validate_non_zero(second)
        result = first % second
        self._record_history(f"{first} % {second} = {result}")
        return result

    def floor_divide(self, first: float, second: float) -> float:
        Validator.validate_non_zero(second)
        result = first // second
        self._record_history(f"{first} // {second} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        result = base ** exponent
        self._record_history(f"{base} ** {exponent} = {result}")
        return result

    # Scientific operations

    def square_root(self, value: float) -> float:
        if value < 0:
            raise ValidationError(
                "Cannot calculate the square root of a negative number."
            )
        result = math.sqrt(value)
        self._record_history(f"sqrt({value}) = {result}")
        return result

    def factorial(self, value: int) -> int:
        result = math.factorial(value)
        self._record_history(f"{value}! = {result}")
        return result

    def percentage(self, part: float, whole: float) -> float:
        Validator.validate_non_zero(whole)
        result = (part / whole) * 100
        self._record_history(f"{part} is {result:.2f}% of {whole}")
        return result

    def sine(self, degrees: float) -> float:
        result = math.sin(math.radians(degrees))
        self._record_history(f"sin({degrees}) = {result}")
        return result

    def cosine(self, degrees: float) -> float:
        result = math.cos(math.radians(degrees))
        self._record_history(f"cos({degrees}) = {result}")
        return result

    def tangent(self, degrees: float) -> float:
        result = math.tan(math.radians(degrees))
        self._record_history(f"tan({degrees}) = {result}")
        return result

    def natural_log(self, value: float) -> float:
        if value <= 0:
            raise ValidationError(
                "Logarithm is only defined for positive numbers."
            )
        result = math.log(value)
        self._record_history(f"ln({value}) = {result}")
        return result

    def log_base_10(self, value: float) -> float:
        if value <= 0:
            raise ValidationError(
                "Logarithm is only defined for positive numbers."
            )
        result = math.log10(value)
        self._record_history(f"log10({value}) = {result}")
        return result

    # Expression evaluation

    def evaluate_expression(self, expression: str) -> float:
        
        try:
            result = eval(expression, {"__builtins__": {}}, {})
        except ZeroDivisionError:
            raise ValidationError("Division by zero is not allowed.")
        except Exception:
            raise ValidationError("Could not evaluate the expression.")
        self._record_history(f"{expression} = {result}")
        return result

    # Memory functions

    def memory_store(self, value: float) -> None:
        self._memory = value

    def memory_recall(self) -> float:
        return self._memory

    def memory_clear(self) -> None:
        self._memory = 0.0

    # History functions

    def _record_history(self, entry: str) -> None:
        self._history.append(entry)

    def get_history(self) -> list:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()