import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to append a character to the entry field
def append_to_entry(char):
    entry.insert(tk.END, char)

# Function for square root
def square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function for exponentiation
def exponentiate():
    try:
        base, exp = map(float, entry.get().split('^'))
        result = base ** exp
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry field
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Place buttons on the grid
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: append_to_entry(x) if x != '=' else evaluate_expression()
    tk.Button(root, text=button, padx=20, pady=20, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
tk.Button(root, text='C', padx=20, pady=20, command=clear_entry).grid(row=row_val, column=0)
tk.Button(root, text='√', padx=20, pady=20, command=square_root).grid(row=row_val, column=1)
tk.Button(root, text='^', padx=20, pady=20, command=exponentiate).grid(row=row_val, column=2)

# Run the main loop
root.mainloop()
