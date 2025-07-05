import tkinter as tk
from tkinter import messagebox

# initialze the root window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

#User display
entry_variable = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_variable, font="Arial 18",
                 justify = "right", bd = 10, relief = tk.SUNKEN)
entry.pack(fill = tk.BOTH, ipadx = 8, ipady = 8, padx = 10, pady = 10)

# start the Tkinter event loop
root.mainloop()
