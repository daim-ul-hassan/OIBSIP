import tkinter as tk
import sqlite3
from datetime import datetime 
import matplotlib.pyplot as plt

root = tk.Tk()

connection = sqlite3.connect("bmi_records.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        bmi REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )
""")

connection.commit()

result_var = tk.StringVar()

result_display = tk.Label(
    root,
    textvariable = result_var,
    font = ("Arial",14,"bold")
)

result_display.pack(pady=20)

root.title("BMI Calculator")
root.geometry("750x750")

title = tk.Label(
    root,
    text = "BMI CALCULATOR",
    font = ("Arial",18,"bold")
)

title.pack(pady=20)

name_label = tk.Label(
    root,
    text = "Name: "
)

name_label.pack(pady=(20,5))

name_entry = tk.Entry(
    root,
    width=20
)

name_entry.pack()

weight_label = tk.Label(
    root,
    text = "Weight (Kg):"
)

weight_label.pack(pady=(20,5))

weight_entry = tk.Entry(
    root,
    width=20
)

weight_entry.pack()

height_label = tk.Label(
    root,
    text="Height (m):"
)

height_label.pack(pady=(20,5))

height_entry = tk.Entry(
    root,
    width=20
)

height_entry.pack()

def calculate_bmi():
    try:
        name = name_entry.get().strip()

        if not name:
            result_var.set("Error: Please enter a name.")
            result_display.config (fg="red")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            result_var.set("Error: Weight and height must be greater than 0.")
            result_display.config(fg="red")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            result_color = "orange"

        elif bmi < 25:
            category = "Normal"
            result_color = "green"

        elif bmi < 30:
            category = "Overweight"
            result_color = "orange"

        else:
            category = "Obese"
            result_color = "red"

        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            cursor.execute(
                "INSERT INTO bmi_records (name, weight, height, bmi, category, date) VALUES (?, ?, ?, ?, ?, ?)",
                (name,weight,height,bmi,category,current_date)
            )

            connection.commit()

        except sqlite3.Error:
            connection.rollback()
            result_var.set("Error: Could not save BMI record.")
            result_display.config(fg="red")
            return

        result_var.set("Name: " + name + "\nBMI: " + str(round(bmi,2)) + "\nCategory: " + category)
        result_display.config(fg=result_color)

    except ValueError:
        result_var.set("Error: Please enter valid numbers.")
        result_display.config(fg="red")
    
def show_history():
    name = name_entry.get().strip()

    if not name:
        result_var.set("Error: Please enter a name.")
        result_display.config(fg="red")
        return

    try:
        cursor.execute(
            "SELECT weight, height, bmi, category, date FROM bmi_records WHERE name = ? ORDER BY date",
            (name,)
        )

        records = cursor.fetchall()

    except sqlite3.Error:
        result_var.set("Error: Could not read BMI history.")
        result_display.config(fg="red")
        return

    if not records:
        result_var.set("No records found for " + name)
        result_display.config(fg="red")
        return

    history = "History for " + name + ":\n\n"

    for record in records:
        weight,height,bmi,category,date = record

        history += (
            "Date: " + date +
            "\nWeight: " + str(weight) + " kg" +
            "\nHeight: " + str(height) + " m" +
            "\nBMI: " + str(round(bmi,2)) +
            "\nCategory: " + category +
            "\n\n"
        )

    result_var.set(history)
    result_display.config(fg="black")

def show_graph():
    name = name_entry.get().strip()

    if not name:
        result_var.set("Error: Please enter a name.")
        result_display.config(fg="red")
        return

    try:
        cursor.execute(
            "SELECT bmi, date FROM bmi_records WHERE name = ? ORDER BY date",
            (name,)
        )

        records = cursor.fetchall()

    except sqlite3.Error:
        result_var.set("Error: Could not read BMI records.")
        result_display.config(fg="red")
        return

    if not records:
        result_var.set("No records found for " + name)
        result_display.config(fg="red")
        return

    dates = []
    bmi_values = []

    for bmi, date in records:
        dates.append(date)
        bmi_values.append(bmi)

    plt.figure(figsize=(8, 5))
    plt.plot(dates,bmi_values,marker="o")
    plt.title("BMI Trend for " + name)
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
            

calculate_button = tk.Button(
    root,
    text = "Calculate BMI",
    command = calculate_bmi
)

calculate_button.pack(pady=25)

history_button = tk.Button(
    root,
    text = "View History",
    command = show_history
)

history_button.pack(pady=10)

graph_button = tk.Button(
    root,
    text = "View BMI Trend",
    command = show_graph
)

graph_button.pack(pady=10)

root.mainloop()
