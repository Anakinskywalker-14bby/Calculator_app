# Simple Calculator App in Python

This project is a user-friendly calculator application built with Python and the Tkinter library. It provides a graphical user interface (GUI) for performing basic arithmetic operations, including addition, subtraction, multiplication, and division. The calculator features a clean display for user input and results, a grid of buttons for digits (0-9), operators (+, -, *, /), a clear button (C), and an equals button (=) for calculations.

This README highlights the application's functionality, the skills demonstrated through its development, and opportunities for further customization.

---

## Table of Contents

- [Application Overview](#application-overview)
- [Skills Demonstrated](#skills-demonstrated)
- [Running the Application](#running-the-application)
- [Customization and Extensions](#customization-and-extensions)

---

## Application Overview

The Simple Calculator App is designed to mimic a standard handheld calculator, providing an intuitive interface for users to perform mathematical calculations. Key features include:

- **Interactive GUI:** A window with a text entry field at the top displays user inputs and results. Below it, a grid of buttons allows users to input digits, operators, and control functions.
- **Arithmetic Operations:** Supports addition (+), subtraction (-), multiplication (*), and division (/), enabling users to perform calculations like `7 + 5` or `100 / 4`.
- **Clear Functionality:** A "C" button resets the display to an empty state, allowing users to start a new calculation.
- **Error Handling:** Invalid inputs, such as division by zero (e.g., `100 / 0`), trigger a pop-up error message to inform the user of the issue.
- **Event-Driven Design:** Clicking buttons triggers specific actions, such as appending digits to the input string, clearing the display, or evaluating the expression when "=" is pressed.

---

## Skills Demonstrated

Building this calculator app showcases a range of programming and software development skills, including:

- **Python Programming:** Utilizing Python for core logic, including string manipulation, event handling, and expression evaluation using the `eval` function.
- **GUI Development with Tkinter:** Creating a graphical interface with Tkinter's `Tk`, `Entry`, `Button`, and `Frame` widgets, demonstrating layout management and widget configuration.
- **Event-Driven Programming:** Implementing an `on_click` function to handle user interactions (e.g., button clicks) and dynamically update the display based on events.
- **Nested Data Structures:** Using a list of lists to define the button grid layout, showcasing data organization and iteration with nested loops.
- **Error Handling:** Employing `try-except` blocks to catch and handle exceptions (e.g., invalid mathematical expressions), enhancing user experience with clear error messages via `messagebox`.
- **Git Version Control:** Managing the project with Git, including initializing a repository, committing changes, and pushing to a remote GitHub repository, demonstrating version control proficiency.
- **Virtual Environment Management:** Setting up and using a virtual environment to isolate project dependencies, ensuring a clean and conflict-free development environment.
- **UI/UX Design Principles:** Designing an intuitive interface with aligned text, consistent fonts, and a 3D visual effect (e.g., `relief="sunken"` for the display), prioritizing usability and aesthetics.

---

## Running the Application

### Ensure Prerequisites

- Python 3.x is installed.
- Visual Studio Code (VS Code) is set up with the Python extension.
- The project folder (e.g., `E:\Python Projects\Calculator`) contains `calculator_app.py` and a `.gitignore` file.

### Activate the Virtual Environment

Open the VS Code terminal (`Ctrl + ~`) and run:

```
.\venv\Scripts\activate
```

### Run the Application

Open `calculator_app.py` in VS Code.  
Click the Run button or execute in the terminal:

```
python calculator_app.py
```

### Interact with the Calculator

- Click number and operator buttons to build expressions (e.g., `7 + 5`).
- Press `=` to compute and display the result.
- Press `C` to clear the display.
- Invalid operations (e.g., `100 / 0`) trigger an error pop-up.

---

## Customization and Extensions

The calculator app offers several opportunities for enhancement:

- **Enhanced Visuals:** Adjust font sizes, colors, or button styles (e.g., `relief="raised"`, `bd=5`) to create a personalized look and feel.
- **Additional Operations:** Expand the button grid to include advanced operations like exponentiation (`**`), modulo (`%`), or square roots, enabling more complex calculations.
- **Custom Error Messages:** Refine error handling to display specific messages (e.g., "Division by Zero" or "Invalid Expression") for different error types.
- **Keyboard Input Support:** Add key bindings to allow users to input numbers and operators via the keyboard, improving accessibility.
- **History Feature:** Implement a feature to store and display previous calculations, enhancing functionality for frequent users.

---