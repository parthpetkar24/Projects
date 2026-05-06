# 🧮 Simple Calculator

A command-line calculator built in Python that supports basic arithmetic, advanced trigonometric operations, and persistent calculation history via JSON.

---

## Features

- **Basic Arithmetic** — Addition, Subtraction, Multiplication, Division
- **Advanced Trigonometry** — Sine, Cosine, Tangent, Cosecant, Secant, Cotangent
- **Chained Calculations** — The result of each operation is automatically carried forward as the first operand for the next
- **History Logging** — Save the current result with a timestamp to a local `data.json` file
- **View History** — Display all previously saved results within the session
- **Clear / Reset** — Save the current state to history and reset the calculator to zero

---

## Project Structure

Calculator
├── calculator.py   # Main application script
└── data.json       # Auto-generated history file (created on first save)
```

---

## Requirements

- Python 3.10 or higher (uses `match`/`case` syntax)
- No external dependencies — only standard library modules (`math`, `json`, `datetime`, `os`)

---

## Getting Started

Clone or download the project, then run:

```bash
python calculator.py
```

---

## Usage

On launch, you'll see a menu of available operations:

```
Operation Available: 1.Add  2.Subtract  3.Multiply  4.Divide  5.Advanced  6.Clear  7.History  8.Exit
```

| Option | Operation   | Description                                              |
|--------|-------------|----------------------------------------------------------|
| 1      | Add         | Adds two numbers                                         |
| 2      | Subtract    | Subtracts second number from first                       |
| 3      | Multiply    | Multiplies two numbers                                   |
| 4      | Divide      | Divides first number by second                           |
| 5      | Advanced    | Opens trigonometric sub-menu                             |
| 6      | Clear       | Saves current result to history, resets storage to `0`  |
| 7      | History     | Displays all saved history entries from `data.json`      |
| 8      | Exit        | Exits the program                                        |

### Chained Calculations

After the first operation, the result is stored and automatically used as the first number in subsequent operations — no need to re-enter it.

### Advanced (Trigonometric) Sub-menu

| Option | Function   |
|--------|------------|
| 1      | Sine       |
| 2      | Cosine     |
| 3      | Tangent    |
| 4      | Cosecant   |
| 5      | Secant     |
| 6      | Cotangent  |

> **Note:** Trig functions operate on the current stored result (in radians).

---

## History File

Calculation history is stored in `data.json` in the same directory as `calculator.py`. Each entry records the timestamp and the result at the time of saving.

Example json
[
    {
        "datetime": "2026-05-06 09:17:07",
        "last_result": 4.0
    },
    {
        "datetime": "2026-05-06 09:17:27",
        "last_result": 12.0
    }
]
```

---

## Known Limitations

- Trig functions that approach undefined values (e.g., `tan(π/2)`) may return very large numbers
- Invalid operation input after an error may cause an `UnboundLocalError` on `user_in`

---
