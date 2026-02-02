# Python Banking System – Fundamentals Practice

This repository contains a **terminal-based banking system** developed in Python as a **learning reinforcement project**, with a focus on strengthening core programming fundamentals.

The project was intentionally kept simple to prioritize clarity, correctness, and good practices over complexity. It serves as a solid foundation for future enhancements.

---

## 📌 Project Overview

The application simulates a basic banking system that runs in the terminal, allowing the user to:

* Deposit money
* Withdraw money
* Check the current balance
* Exit the system safely

All interactions are handled via user input, with validation to prevent invalid operations or unexpected program crashes.

---

## 🎯 Learning Goals

This project was created to reinforce essential Python concepts, including:

* Programming logic and flow control
* Input validation and error handling
* Code organization using functions
* Separation between user input handling and business rules

Rather than introducing advanced libraries or frameworks, the focus is on mastering the basics that support more complex systems later on.

---

## 🧠 Concepts Applied

### Loops

* The program uses a `while True` loop to keep running until the user explicitly chooses to exit.
* The loop is controlled using `break` when the exit option is selected.

### Functions

* Functions are used to:

  * Avoid code repetition
  * Improve readability
  * Centralize logic (such as input validation)

Examples include functions for printing formatted lines and safely reading numeric input.

### Exception Handling (`try/except`)

* User inputs are validated using `try/except` blocks to prevent runtime errors when non-numeric values are entered.
* This ensures the program remains stable and user-friendly.

### Type Conversion (Casting)

* Inputs are converted to the appropriate numeric types (`int` and `float`) only after validation.

### Conditional Structures

* `if`, `elif`, and `else` statements control the program flow and determine which banking operation is executed.

### Business Rule Validation

* The system prevents:

  * Deposits with zero or negative values
  * Withdrawals with zero or negative values
  * Withdrawals that exceed the available balance
  * Invalid menu options

---

## 🖥️ How the Program Works

1. The user is presented with a menu of options.
2. The program waits for a valid numeric option.
3. Based on the selected option:

   * A deposit, withdrawal, or balance check is performed
   * Or the program exits gracefully
4. The system continues running until the user chooses to exit.

All user inputs are validated to ensure safe execution.

---

## 🚀 Future Improvements

This project is a starting point. Planned future enhancements include:

* Adding **data persistence** (saving balance and transactions to a file or database)
* Implementing a **transaction history**
* Refactoring business logic into separate modules
* Improving the user interface

These improvements will gradually move the project closer to a real-world application while maintaining a strong foundation.

---

## 🛠️ Technologies Used

* Python 3
* Standard Library only (no external dependencies)

---

## 📚 Purpose

This repository exists primarily as a **learning artifact**, demonstrating the importance of revisiting and reinforcing programming fundamentals. A strong base makes it easier to scale, refactor, and evolve software over time.

---

## 👤 Author

Developed as part of a personal learning journey in Python and software development fundamentals.

---

Feel free to explore, study, and build upon this project.
