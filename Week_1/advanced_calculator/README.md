# 🧮 Advanced Command-Line Calculator

A menu-driven Python calculator that combines everyday arithmetic, scientific
functions, safe expression evaluation, memory storage, and calculation
history in a clean, color-styled console interface.

## ✨ Features

- ➕ **Basic arithmetic** — addition, subtraction, multiplication, division, modulus, floor division, exponentiation
- 🔬 **Scientific functions** — square root, factorial, percentage, sine, cosine, tangent, natural log, log base 10
- 💻 **Expression evaluator** — safely evaluates expressions like `3 + 4 * 2` after strict character validation
- 🧠 **Memory register** — store, recall, and clear a single value
- 📝 **Calculation history** — view or clear a log of every successful operation
- ✅ **Input validation** — centralized checks with clear, non-crashing error messages
- 🎨 **Styled console UI** — boxed panels, colored output, and a categorized 21-option menu

## 🛠️ Technologies Used

- 🐍 Python 3 (standard library only)
- 📐 `math` — scientific and trigonometric operations
- 🔍 `re` — expression character validation
- 🖥️ `os` — clearing the terminal screen
- 🌈 ANSI escape codes for console styling

## 📁 Project Structure

```text
├── main.py         # ConsoleUI, Colors, and CalculatorApp — menu, I/O, and app loop
├── calculator.py   # Calculator class — arithmetic, scientific ops, memory, history
└── validator.py    # Validator class and ValidationError — centralized input validation
```

## 🚀 How to Run the Project

Requires Python 3 and no external dependencies.

```bash
python main.py
```

## 🖥️ Sample Menu

```text
┌────────────────────────────────────────────────────────────────┐
│               ADVANCED COMMAND-LINE CALCULATOR                 │
│              Arithmetic • Scientific • Expressions             │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                          MAIN MENU                             │
├────────────────────────────────────────────────────────────────┤
│ ▸ Basic Arithmetic                                             │
│  1. Addition               2. Subtraction                      │
│  3. Multiplication         4. Division                         │
│  ...                                                           │
│ ▸ Scientific Functions                                         │
│  8. Square Root             9. Factorial                       │
│  ...                                                           │
│  0. Exit                                                       │
└────────────────────────────────────────────────────────────────┘
➤ Enter your choice: 1
➤ Enter the first number: 12
➤ Enter the second number: 8

┌────────────────────────────────────────────────────────────────┐
│ RESULT — Addition                                              │
├────────────────────────────────────────────────────────────────┤
│ 20.0                                                           │
└────────────────────────────────────────────────────────────────┘
```

## 🔮 Future Improvements

- 💾 Persist calculation history to a file between sessions
- 🧠 Add support for multiple memory slots
- 🧪 Add unit tests for `Calculator` and `Validator`

## 👩‍💻 Author

**Noor Alishba Sajid**  
BS Artificial Intelligence, University of Engineering and Technology (UET) Lahore