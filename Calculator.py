import math
import tkinter as tk
from tkinter import messagebox

def on_click(event):
    # This function handles button click events
    text = event.widget.cget("text")  # Get the text label of the button that was clicked
    if text == "=":
        try:
            result = eval(str(entry_variable.get()))  # Evaluate the string as a Python expression
            entry_variable.set(result)  # Display the result in the entry field
        except Exception:
            # If there is an error, show an error message
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry_variable.set("")
    elif text == "x²":
        result = eval(str(entry_variable.get()) + "**2")  
        entry_variable.set(result) 
    elif text == "π":
        result = eval(str(entry_variable.get()) + "*math.pi")  
        entry_variable.set(result)
    elif text == "√":
        try:
            value = float(entry_variable.get())
            result = math.sqrt(value)
            entry_variable.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    else:
        # For all other buttons (numbers and operators), append their text to the entry field
        entry_variable.set(entry_variable.get() + text)

# Initialize the root window for the calculator app
root = tk.Tk()  # Create the main application window
root.title("Calculator")  # Set the window title
root.geometry("400x500")  # Set the window size (width x height in pixels)

# User display
entry_variable = tk.StringVar()  # Create a StringVar to hold the text shown in the entry field
entry = tk.Entry(
    root,  # Parent widget is the main window
    textvariable=entry_variable,  # Link the entry field to the StringVar
    font="Arial 18",  # Set the font and size for the text
    justify="right",  # Align text to the right (like a real calculator)
    bd=10,  # Set border width
    relief=tk.SUNKEN  # Give the entry field a sunken 3D effect
)
entry.pack(
    fill=tk.BOTH,  # Make the entry expand to fill available space horizontally and vertically
    ipadx=10,  # Add internal padding in x-direction
    ipady=10,  # Add internal padding in y-direction
    padx=10,  # Add external padding in x-direction
    pady=10   # Add external padding in y-direction
)

# Button configuration
buttons_list = [
    [".", "x²", "π", "√"], 
    ["7", "8", "9", "/"],  
    ["4", "5", "6", "*"],  
    ["1", "2", "3", "-"],  
    ["C", "0", "=", "+"], 
]

# Create the button grid
for row in buttons_list:
    button_frame = tk.Frame(root)  # Create a new frame for each row of buttons
    button_frame.pack(expand=True, fill=tk.BOTH)  # Make the row expand to fill available space
    for button_text in row:
        button = tk.Button(
            button_frame,  # Parent widget is the current row's frame
            text=button_text,  # Set the button's label
            font="Arial 18",  # Set the font and size for the button text
            relief=tk.RIDGE,  # Give the button a raised 3D effect
            bd=3  # Set border width for the button
        )
        button.pack(
            side=tk.LEFT,  # Align buttons to the left within the row
            expand=True,  # Make buttons expand to fill available space in the row
            fill=tk.BOTH  # Fill both horizontally and vertically
        )
        button.bind("<Button-1>", on_click)  # Bind left mouse click to the on_click function

# Start the Tkinter event loop
root.mainloop()
