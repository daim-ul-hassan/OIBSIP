import secrets
import string
import tkinter as tk
import pyperclip

root = tk.Tk()

root.title("Random Password Generator")
root.geometry("700x700")

title = tk.Label(
    root,
    text = "RANDOM PASSWORD GENERATOR",
    font = ("Arial", 18, "bold")
)

title.pack(pady=20)

welcome = tk.Label(
    root,
    text = "Welcome! Let's generate a random password.",
    font = ("Arial", 11)
)

length_label = tk.Label(
    root,
    text = "Password Length:"
)

strength_var = tk.StringVar(value="Strength: ")

strength_display = tk.Label(
    root,
    textvariable = strength_var,
    font = ("Arial", 12, "bold")
)

length_label.pack(pady=(30,5))

length_spinbox = tk.Spinbox(
    root,
    from_=8,
    to=64,
    width=10
)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=False)
symbols_var = tk.BooleanVar(value=False)
exclude_ambiguous_var = tk.BooleanVar(value=False)

uppercase_check = tk.Checkbutton(
    root,
    text = "Uppercase letters",
    variable = uppercase_var
)

lowercase_check = tk.Checkbutton(
    root,
    text = "Lowercase letters",
    variable = lowercase_var
)

numbers_check = tk.Checkbutton(
    root,
    text = "Numbers",
    variable = numbers_var
)

symbols_check = tk.Checkbutton(
    root,
    text = "Symbols",
    variable = symbols_var
)

exclude_ambiguous_check = tk.Checkbutton(
    root,
    text = "Exclude ambiguous characters (0, O, l, 1)",
    variable = exclude_ambiguous_var
)

password_var = tk.StringVar()
password_history = []

def copy_password():
    pyperclip.copy(password_var.get())

copy_button = tk.Button(
    root,
    text = "Copy to Clipboard",
    command = copy_password
)


def generate_password():
    password_length = int(length_spinbox.get())

    selected_types = 0

    if uppercase_var.get():
        selected_types += 1

    if lowercase_var.get():
        selected_types += 1

    if numbers_var.get():
        selected_types += 1

    if symbols_var.get():
        selected_types += 1

    if selected_types < 2:
        strength_var.set("Error: Select at least 2 character types.")
        return

    character_pool = ""

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    number_chars = string.digits

    if exclude_ambiguous_var.get():
        uppercase_chars = uppercase_chars.replace("O", "")
        lowercase_chars = lowercase_chars.replace("l", "")
        number_chars = number_chars.replace("0", "").replace("1", "")

    if uppercase_var.get():
        character_pool += uppercase_chars

    if lowercase_var.get():
        character_pool += lowercase_chars

    if numbers_var.get():
        character_pool += number_chars

    if symbols_var.get():
        character_pool += string.punctuation

    password = ""

    if uppercase_var.get():
        password += secrets.choice(uppercase_chars)
    
    if lowercase_var.get():
        password += secrets.choice(lowercase_chars)

    if numbers_var.get():
        password += secrets.choice(number_chars)

    if symbols_var.get():
        password += secrets.choice(string.punctuation)

    for i in range(password_length - len(password)):
        password += secrets.choice(character_pool)

    password_var.set(password)

    password_history.append(password)

    if len(password_history) > 5:
        password_history.pop(0)

    history_var.set("\n".join(password_history))

    pyperclip.copy(password)

    if password_length < 10 or selected_types == 2:
        strength_var.set("Strength: Weak")
        strength_display.config(fg="red")

    elif password_length < 16 and selected_types >= 3:
        strength_var.set("Strength: Medium")
        strength_display.config(fg="orange")

    else:
        strength_var.set("Strength: Strong")
        strength_display.config(fg="green")

password_display = tk.Label(
    root,
    textvariable = password_var,
    font = ("Arial",14)
)

history_label = tk.Label(
    root,
    text = "Generation History",
    font = ("Arial",11,"bold")
)

history_var = tk.StringVar()

history_display = tk.Label(
    root,
    textvariable = history_var,
    font = ("Arial",10),
    justify = "left"
)

history_display.pack()

history_label.pack(pady =(20,5))

password_display.pack(pady=10)

generate_button = tk.Button(
    root,
    text = "Generate Password",
    command = generate_password
)

generate_button.pack(pady=20)

strength_display.pack()

copy_button.pack()

uppercase_check.pack()
lowercase_check.pack()
numbers_check.pack()
symbols_check.pack()
exclude_ambiguous_check.pack()

length_spinbox.pack()

welcome.pack()

root.mainloop()