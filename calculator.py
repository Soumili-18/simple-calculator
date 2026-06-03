import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button_text))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda b=button: click(b)

    tk.Button(
        root,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root,
    text="C",
    width=22,
    height=2,
    font=("Arial", 16),
    command=clear
).grid(row=row, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()