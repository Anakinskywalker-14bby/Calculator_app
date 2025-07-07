import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_variable.get()))
            entry_variable.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    
    elif text == "C":
        entry_variable.set("")
        
    else:
        entry_variable.set(entry_variable.get() + text)

# Initialize the root window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# User display
entry_variable = tk.StringVar()
entry = tk.Entry(root, textvariable = entry_variable, font = "Arial 18",
                 justify = "right", bd = 10, relief = tk.SUNKEN)
entry.pack(fill = tk.BOTH, ipadx = 10, ipady = 10, padx = 10, pady = 10)

# Button configuration
buttons_list = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

for row in buttons_list:
    button_frame = tk.Frame(root)
    button_frame.pack(expand = True, fill = tk.BOTH)
    for button_text in row:
        button = tk.Button(button_frame, text = button_text, 
                           font = "Arial 18", relief = tk.RIDGE, bd = 3)
        button.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        button.bind("<Button-1>", on_click)

# start the Tkinter event loop
root.mainloop()
