"""
validator.py

Provides centralized validation utilities for the command-line calculator.
"""

import re

class ValidationError(Exception):
    pass


class Validator:

    _ALLOWED_EXPRESSION_PATTERN = re.compile(r'^[\d.\+\-\*/%\(\)\s]+$')

    @staticmethod
    def validate_number(raw_value: str) -> float:
        
        try:
            return float(raw_value)
        except (TypeError, ValueError):
            raise ValidationError(f"'{raw_value}' is not a valid number.")

    @staticmethod
    def validate_integer(raw_value: str) -> int:
        
        try:
            return int(raw_value)
        except (TypeError, ValueError):
            raise ValidationError(f"'{raw_value}' is not a valid integer.")

    @staticmethod
    def validate_non_negative_integer(raw_value: str) -> int:
        
        number = Validator.validate_integer(raw_value)
        if number < 0:
            raise ValidationError("Value must be a non-negative integer.")
        return number

    @staticmethod
    def validate_non_zero(value: float) -> float:
       
        if value == 0:
            raise ValidationError("Division by zero is not allowed.")
        return value

    @staticmethod
    def validate_menu_choice(raw_choice: str, valid_choices: set) -> str:
        
        choice = raw_choice.strip()
        if choice not in valid_choices:
            raise ValidationError("Invalid menu choice. Please try again.")
        return choice

    @staticmethod
    def validate_expression(raw_expression: str) -> str:
        
        expression = raw_expression.strip()
        if not expression:
            raise ValidationError("Expression cannot be empty.")
        if not Validator._ALLOWED_EXPRESSION_PATTERN.match(expression):
            raise ValidationError(
                "Expression contains invalid characters. "
                "Only digits, +, -, *, /, %, (, ) and spaces are allowed."
            )
        return expression