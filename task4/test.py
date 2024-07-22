import tkinter as tk
from tkinter import messagebox


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        messagebox.showerror("Error", "Division by zero is not allowed")
        return None


def evaluate_expression():
    try:
        result = eval(expression.get())
        result_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_expression(value):
    current_expression = expression.get()
    expression.set(current_expression + str(value))


def clear_expression():
    expression.set("")


root = tk.Tk()
root.title("3D Calculator")


bg_color = "#000000"  
fg_color = "#FFA500"  

root.configure(bg=bg_color)


expression = tk.StringVar()
result_var = tk.StringVar()


entry = tk.Entry(root, textvariable=expression, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4, bg=bg_color, fg=fg_color, highlightbackground=fg_color, highlightcolor=fg_color)
entry.grid(row=0, column=0, columnspan=4, pady=10)


result_entry = tk.Entry(root, textvariable=result_var, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4, bg=bg_color, fg=fg_color, highlightbackground=fg_color, highlightcolor=fg_color, state='readonly')
result_entry.grid(row=1, column=0, columnspan=4, pady=10)


buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
    ('C', 6, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=evaluate_expression, bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=clear_expression, bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: update_expression(t), bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color)
    button.grid(row=row, column=col, padx=5, pady=5)


root.mainloop()
