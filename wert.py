import math
import tkinter as tk

window = tk.Tk()
window.title("my scientific calculator")
window.configure(bg="black")

display = tk.Entry(
    window,
    width=30,
    font=("Arial", 20),
    justify="right",
    bg="white",
    fg="black",
)
display.grid(row=0, column=0, columnspan=5)


def insert(text):
    display.insert("end", text)


def clear():
    display.delete(0, "end")


def calculate():
    expression = display.get()
    # Convert what the user sees into something Python understands
    expression = expression.replace("^", "**")
    try:
        result = eval(
            expression,
            {"__builtins__": {}},  # block access to other Python functions
            {"sqrt": math.sqrt, "log": math.log10},
        )
    except ZeroDivisionError:
        result = "Error: divide by 0"
    except Exception:
        result = "Error"
    clear()
    insert(str(result))


# (label, row, column, action)
buttons = [
    ("1", 1, 0, lambda: insert("1")),
    ("2", 1, 1, lambda: insert("2")),
    ("3", 1, 2, lambda: insert("3")),
    ("c", 1, 3, clear),
    ("+", 1, 4, lambda: insert("+")),

    ("4", 2, 0, lambda: insert("4")),
    ("5", 2, 1, lambda: insert("5")),
    ("6", 2, 2, lambda: insert("6")),
    ("-", 2, 3, lambda: insert("-")),
    ("*", 2, 4, lambda: insert("*")),

    ("7", 3, 0, lambda: insert("7")),
    ("8", 3, 1, lambda: insert("8")),
    ("9", 3, 2, lambda: insert("9")),
    ("/", 3, 3, lambda: insert("/")),
    ("log", 3, 4, lambda: insert("log(")),

    (".", 4, 0, lambda: insert(".")),
    ("0", 4, 1, lambda: insert("0")),
    ("=", 4, 2, calculate),
    ("^", 4, 3, lambda: insert("^")),
    ("sqrt", 4, 4, lambda: insert("sqrt(")),

    ("(", 5, 0, lambda: insert("(")),
    (")", 5, 1, lambda: insert(")")),
]

for text, row, col, action in buttons:
    tk.Button(
        window,
        text=text,
        command=action,
        width=5,
        height=2,
        padx=5,
        pady=5,
        bg="yellow",
        fg="black",
    ).grid(row=row, column=col)

# Press Enter on the keyboard to calculate
window.bind("<Return>", lambda event: calculate())

window.mainloop()