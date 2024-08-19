
import tkinter as tk

# Function to update the expression in the entry field
def click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_value)

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the expression
entry = tk.Entry(root, width=16, borderwidth=3, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and properties
buttons = [
    ('7', "#f0f0f0", "#000000"),
    ('8', "#f0f0f0", "#000000"),
    ('9', "#f0f0f0", "#000000"),
    ('/', "#9bdeac", "#000000"),
    ('4', "#f0f0f0", "#000000"),
    ('5', "#f0f0f0", "#000000"),
    ('6', "#f0f0f0", "#000000"),
    ('*', "#9bdeac", "#000000"),
    ('1', "#f0f0f0", "#000000"),
    ('2', "#f0f0f0", "#000000"),
    ('3', "#f0f0f0", "#000000"),
    ('-', "#9bdeac", "#000000"),
    ('0', "#f0f0f0", "#000000"),
    ('.', "#9bdeac", "#000000"),
    ('=', "#004d00", "#ffffff"),
    ('+', "#9bdeac", "#000000")
]

# Place buttons on the window with custom colors and cursor pointer
row = 1
col = 0
for (button, bg_color, fg_color) in buttons:
    tk.Button(
        root, text=button, width=5, height=2, font=('Arial', 18),
        bg=bg_color,  # Background color
        fg=fg_color,  # Text color
        cursor="hand2",  # Cursor pointer (hand2 changes cursor to a hand)
        command=lambda b=button: click(b) if b != '=' else evaluate()
    ).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add Clear button with custom colors and cursor pointer
tk.Button(
    root, text='C', width=5, height=2, font=('Arial', 18),
    bg="#ff6666",  # Background color for Clear button
    fg="#ffffff",  # Text color for Clear button
    cursor="hand2",  # Cursor pointer
    command=clear
).grid(row=row, column=col)

# Run the application
root.mainloop()
