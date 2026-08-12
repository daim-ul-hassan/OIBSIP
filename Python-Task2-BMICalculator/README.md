# BMI Calculator

A Python BMI Calculator project built for the OIBSIP Python Programming Internship.

The project includes both a Beginner command-line version and an Advanced GUI version with SQLite storage and BMI trend visualization.

## Project Versions

### Beginner Version

The Beginner version is a simple command-line BMI calculator built using basic Python.

Features:

- Takes weight in kilograms
- Takes height in meters
- Calculates BMI
- Classifies BMI into standard categories
- Displays BMI rounded to 2 decimal places
- Validates non-numeric input
- Rejects zero and negative values

### Advanced Version

The Advanced version includes all Beginner features plus a full graphical interface and additional functionality.

Features:

- Tkinter GUI
- Named user support
- Weight and height input fields
- BMI calculation
- Colour-coded BMI results
- Input validation
- Multiple user support
- SQLite database storage
- Historical BMI records
- BMI trend visualization using Matplotlib
- Database read/write error handling
- Records persist between application sessions

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25 - 29.9 | Overweight |
| 30 or above | Obese |

## Technologies Used

### Beginner

- Python

### Advanced

- Python
- Tkinter
- SQLite
- Matplotlib

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── bmi.py
├── advanced-bmi.py
├── README.md
├── requirements.txt
└── .gitignore