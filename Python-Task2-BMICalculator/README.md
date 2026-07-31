# BMI Calculator

## Project Information

* **Name:** Muhammad Daim-ul-Hassan
* **Track:** Python
* **Task:** 2
* **Task Name:** BMI Calculator

## Overview

This project is a simple Python BMI Calculator created as part of the Oasis Infobyte Python Internship. The program takes a user's weight and height, calculates their Body Mass Index (BMI), validates the input and classifies the result into the appropriate health category.

## Features

* Prompts the user to enter their weight in kilograms and height in meters.
* Calculates BMI using the standard formula.
* Displays the BMI value rounded to two decimal places.
* Classifies the BMI as:

  * Underweight
  * Normal
  * Overweight
  * Obese
* Validates user input.
* Rejects non-numeric input with a clear error message.
* Rejects zero and negative values with a clear error message.

## BMI Formula

```text
BMI = Weight (kg) / Height² (m²)
```

## BMI Categories

| BMI Range      | Category    |
| -------------- | ----------- |
| Below 18.5     | Underweight |
| 18.5 to 24.9   | Normal      |
| 25.0 to 29.9   | Overweight  |
| 30.0 and above | Obese       |

## Technologies Used

* Python 3

## How to Run

1. Clone the repository.

2. Open the project folder.

3. Run the following command:

```bash
python bmi.py
```

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── bmi.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Sample Output

```text
Enter your weight (kg): 70
Enter your height (m): 1.75

Your BMI value is: 22.86
Category: Normal
```
