
"""
main.py

Entry point for the Advanced Command-Line Calculator.

"""

import os

from calculator import Calculator
from validator import Validator, ValidationError


class Colors:
    

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"


class ConsoleUI:
    

    BOX_WIDTH = 70
    CONTENT_WIDTH = BOX_WIDTH - 4  
    COLUMN_WIDTH = CONTENT_WIDTH // 2

    # Low-level box-drawing helpers

    @classmethod
    def _top_border(cls, color=Colors.CYAN):
        return f"{color}┌{'─' * (cls.BOX_WIDTH - 2)}┐{Colors.RESET}"

    @classmethod
    def _bottom_border(cls, color=Colors.CYAN):
        return f"{color}└{'─' * (cls.BOX_WIDTH - 2)}┘{Colors.RESET}"

    @classmethod
    def _divider(cls, color=Colors.CYAN):
        return f"{color}├{'─' * (cls.BOX_WIDTH - 2)}┤{Colors.RESET}"

    @classmethod
    def _line(cls, text="", align="left", color=Colors.CYAN,
              text_color=""):
        if align == "center":
            content = text.center(cls.CONTENT_WIDTH)
        elif align == "right":
            content = text.rjust(cls.CONTENT_WIDTH)
        else:
            content = text.ljust(cls.CONTENT_WIDTH)
        reset = Colors.RESET if text_color else ""
        return (f"{color}│ {Colors.RESET}{text_color}{content}{reset}"
                f"{color} │{Colors.RESET}")

    # Screen / banner

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def print_banner(cls):
        print(cls._top_border())
        print(cls._line("ADVANCED COMMAND-LINE CALCULATOR", "center",
                         text_color=Colors.BOLD + Colors.CYAN))
        print(cls._line("Arithmetic  \u2022  Scientific  \u2022  Expressions",
                         "center", text_color=Colors.DIM))
        print(cls._bottom_border())
        print()

    # Menu

    @classmethod
    def _menu_row(cls, left, right=""):
        left = left.ljust(cls.COLUMN_WIDTH)
        right = right.ljust(cls.CONTENT_WIDTH - cls.COLUMN_WIDTH)
        return cls._line(left + right)

    @classmethod
    def _menu_section(cls, title, items):
        """Print a titled section of menu options, two per row."""
        print(cls._line(f"\u25b8 {title}",
                         text_color=Colors.BOLD + Colors.YELLOW))
        for index in range(0, len(items), 2):
            left = items[index]
            right = items[index + 1] if index + 1 < len(items) else ""
            print(cls._menu_row(left, right))

    @classmethod
    def print_menu(cls):
        basic = [
            " 1. Addition", " 2. Subtraction",
            " 3. Multiplication", " 4. Division",
            " 5. Modulus (%)", " 6. Floor Division (//)",
            " 7. Exponent (**)",
        ]
        scientific = [
            " 8. Square Root", " 9. Factorial",
            "10. Percentage", "11. Sine",
            "12. Cosine", "13. Tangent",
            "14. Natural Log (ln)", "15. Log Base 10",
        ]
        expression = ["16. Evaluate Expression"]
        memory = [
            "17. Memory Store", "18. Memory Recall",
            "19. Memory Clear",
        ]
        history = ["20. View History", "21. Clear History"]
        exit_option = " 0. Exit"

        print(cls._top_border())
        print(cls._line("MAIN MENU", "center",
                         text_color=Colors.BOLD + Colors.CYAN))
        print(cls._divider())
        cls._menu_section("Basic Arithmetic", basic)
        print(cls._line())
        cls._menu_section("Scientific Functions", scientific)
        print(cls._line())
        cls._menu_section("Expression Evaluator", expression)
        print(cls._line())
        cls._menu_section("Memory Functions", memory)
        print(cls._line())
        cls._menu_section("History", history)
        print(cls._divider())
        print(cls._menu_row(exit_option))
        print(cls._bottom_border())

    # Input prompts

    @staticmethod
    def prompt(text: str) -> str:
        return input(f"{Colors.BLUE}\u27a4 {text}{Colors.RESET}")

    @classmethod
    def ask_menu_choice(cls) -> str:
        print()
        return cls.prompt("Enter your choice: ")

    # Output panels

    @classmethod
    def print_result(cls, label: str, value) -> None:
        print()
        print(cls._top_border(Colors.GREEN))
        print(cls._line(f" RESULT \u2014 {label}", text_color=Colors.BOLD,
                         color=Colors.GREEN))
        print(cls._divider(Colors.GREEN))
        print(cls._line(f" {value}", text_color=Colors.BOLD + Colors.GREEN,
                         color=Colors.GREEN))
        print(cls._bottom_border(Colors.GREEN))

    @classmethod
    def print_success(cls, message: str) -> None:
        print(f"\n{Colors.GREEN}\u2714 {message}{Colors.RESET}")

    @classmethod
    def print_error(cls, message: str) -> None:
        print(f"\n{Colors.RED}\u2716 Error: {message}{Colors.RESET}")

    @classmethod
    def print_info(cls, message: str) -> None:
        print(f"\n{Colors.YELLOW}\u2139 {message}{Colors.RESET}")

    @classmethod
    def print_history(cls, entries: list) -> None:
        print()
        print(cls._top_border(Colors.MAGENTA))
        print(cls._line("CALCULATION HISTORY", "center",
                         color=Colors.MAGENTA,
                         text_color=Colors.BOLD + Colors.MAGENTA))
        print(cls._divider(Colors.MAGENTA))
        if not entries:
            print(cls._line("No calculations have been performed yet.",
                             color=Colors.MAGENTA, text_color=Colors.DIM))
        else:
            for index, entry in enumerate(entries, start=1):
                text = f"{index:>2}. {entry}"
                if len(text) > cls.CONTENT_WIDTH:
                    text = text[:cls.CONTENT_WIDTH - 3] + "..."
                print(cls._line(text, color=Colors.MAGENTA))
        print(cls._bottom_border(Colors.MAGENTA))

    @classmethod
    def pause(cls) -> None:
        input(f"\n{Colors.DIM}Press Enter to return to the main menu..."
              f"{Colors.RESET}")

    @classmethod
    def print_goodbye(cls) -> None:
        print()
        print(cls._top_border(Colors.CYAN))
        print(cls._line("Thank you for using the Advanced Calculator!",
                         "center", text_color=Colors.BOLD + Colors.CYAN))
        print(cls._line("Goodbye.", "center", text_color=Colors.DIM))
        print(cls._bottom_border(Colors.CYAN))


class CalculatorApp:

    def __init__(self):
        self.calculator = Calculator()
        self.ui = ConsoleUI()
        self.running = True
        self.actions = {
            "1": self._handle_add,
            "2": self._handle_subtract,
            "3": self._handle_multiply,
            "4": self._handle_divide,
            "5": self._handle_modulus,
            "6": self._handle_floor_divide,
            "7": self._handle_power,
            "8": self._handle_square_root,
            "9": self._handle_factorial,
            "10": self._handle_percentage,
            "11": self._handle_sine,
            "12": self._handle_cosine,
            "13": self._handle_tangent,
            "14": self._handle_natural_log,
            "15": self._handle_log10,
            "16": self._handle_expression,
            "17": self._handle_memory_store,
            "18": self._handle_memory_recall,
            "19": self._handle_memory_clear,
            "20": self._handle_view_history,
            "21": self._handle_clear_history,
            "0": self._handle_exit,
        }
        
        self._no_pause_actions = {"0"}

    def run(self) -> None:
        """Start the main application loop."""
        self.ui.clear_screen()
        self.ui.print_banner()
        try:
            while self.running:
                self.ui.print_menu()
                raw_choice = self.ui.ask_menu_choice()
                choice = None
                try:
                    choice = Validator.validate_menu_choice(
                        raw_choice, set(self.actions.keys())
                    )
                    self.actions[choice]()
                except ValidationError as error:
                    self.ui.print_error(str(error))
                except Exception as error:
                    
                    self.ui.print_error(f"Unexpected error: {error}")

                if self.running and choice not in self._no_pause_actions:
                    self.ui.pause()
                if self.running:
                    self.ui.clear_screen()
                    self.ui.print_banner()
        except KeyboardInterrupt:
            print()
            self.ui.print_info("Interrupted by user.")
            self.ui.print_goodbye()

    # Input helpers

    def _read_number(self, prompt: str) -> float:
        return Validator.validate_number(self.ui.prompt(prompt))

    def _read_non_negative_integer(self, prompt: str) -> int:
        return Validator.validate_non_negative_integer(self.ui.prompt(prompt))

    # Menu action handlers

    def _handle_add(self):
        a = self._read_number("Enter the first number: ")
        b = self._read_number("Enter the second number: ")
        self.ui.print_result("Addition", self.calculator.add(a, b))

    def _handle_subtract(self):
        a = self._read_number("Enter the first number: ")
        b = self._read_number("Enter the second number: ")
        self.ui.print_result("Subtraction", self.calculator.subtract(a, b))

    def _handle_multiply(self):
        a = self._read_number("Enter the first number: ")
        b = self._read_number("Enter the second number: ")
        self.ui.print_result("Multiplication",
                              self.calculator.multiply(a, b))

    def _handle_divide(self):
        a = self._read_number("Enter the numerator: ")
        b = self._read_number("Enter the denominator: ")
        self.ui.print_result("Division", self.calculator.divide(a, b))

    def _handle_modulus(self):
        a = self._read_number("Enter the first number: ")
        b = self._read_number("Enter the second number: ")
        self.ui.print_result("Modulus", self.calculator.modulus(a, b))

    def _handle_floor_divide(self):
        a = self._read_number("Enter the first number: ")
        b = self._read_number("Enter the second number: ")
        self.ui.print_result("Floor Division",
                              self.calculator.floor_divide(a, b))

    def _handle_power(self):
        base = self._read_number("Enter the base: ")
        exponent = self._read_number("Enter the exponent: ")
        self.ui.print_result("Exponent",
                              self.calculator.power(base, exponent))

    def _handle_square_root(self):
        value = self._read_number("Enter a number: ")
        self.ui.print_result("Square Root",
                              self.calculator.square_root(value))

    def _handle_factorial(self):
        value = self._read_non_negative_integer(
            "Enter a non-negative integer: "
        )
        self.ui.print_result("Factorial", self.calculator.factorial(value))

    def _handle_percentage(self):
        part = self._read_number("Enter the part value: ")
        whole = self._read_number("Enter the whole value: ")
        result = self.calculator.percentage(part, whole)
        self.ui.print_result("Percentage", f"{result:.2f}%")

    def _handle_sine(self):
        degrees = self._read_number("Enter the angle in degrees: ")
        self.ui.print_result("Sine", self.calculator.sine(degrees))

    def _handle_cosine(self):
        degrees = self._read_number("Enter the angle in degrees: ")
        self.ui.print_result("Cosine", self.calculator.cosine(degrees))

    def _handle_tangent(self):
        degrees = self._read_number("Enter the angle in degrees: ")
        self.ui.print_result("Tangent", self.calculator.tangent(degrees))

    def _handle_natural_log(self):
        value = self._read_number("Enter a positive number: ")
        self.ui.print_result("Natural Log",
                              self.calculator.natural_log(value))

    def _handle_log10(self):
        value = self._read_number("Enter a positive number: ")
        self.ui.print_result("Log Base 10",
                              self.calculator.log_base_10(value))

    def _handle_expression(self):
        raw_expression = self.ui.prompt(
            "Enter an expression (e.g. 3 + 4 * 2): "
        )
        expression = Validator.validate_expression(raw_expression)
        result = self.calculator.evaluate_expression(expression)
        self.ui.print_result("Expression", result)

    def _handle_memory_store(self):
        value = self._read_number("Enter the value to store in memory: ")
        self.calculator.memory_store(value)
        self.ui.print_success("Value stored in memory.")

    def _handle_memory_recall(self):
        self.ui.print_result("Memory", self.calculator.memory_recall())

    def _handle_memory_clear(self):
        self.calculator.memory_clear()
        self.ui.print_success("Memory cleared.")

    def _handle_view_history(self):
        self.ui.print_history(self.calculator.get_history())

    def _handle_clear_history(self):
        self.calculator.clear_history()
        self.ui.print_success("History cleared.")

    def _handle_exit(self):
        self.ui.print_goodbye()
        self.running = False


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()