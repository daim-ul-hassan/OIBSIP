# Random Password Generator

A Python project that generates strong random passwords based on user-selected requirements.

This project was created as part of the OIBSIP Python Track, Task 3. It includes both a Beginner command-line version and an Advanced GUI version.

## Project Information

* Name: Muhammad Daim-ul-Hassan
* Track: Python
* Task: 3
* Task Name: Random Password Generator
* Level: Beginner and Advanced

## Versions

### Beginner Version

File:

`random-password-generator.py`

The Beginner version is a command-line password generator built with Python's `random` and `string` modules.

It allows the user to:

* Choose the password length
* Set a minimum password length of 8 characters
* Select uppercase letters
* Select lowercase letters
* Select numbers
* Select symbols
* Require at least 2 character types
* Generate another password without restarting
* Validate user input

### Advanced Version

File:

`advanced-random-password-generator.py`

The Advanced version provides a graphical interface using Tkinter and uses the `secrets` module for secure password generation.

It includes:

* GUI interface
* Password length control from 8 to 64 characters
* Character type selection
* Secure password generation using `secrets`
* At least 2 character types required
* Guaranteed character from every selected type
* Password strength indicator
* Color-coded strength feedback
* Copy to Clipboard
* Automatic clipboard copying after generation
* Option to exclude ambiguous characters such as `0`, `O`, `l` and `1`
* Session history showing the last 5 generated passwords

The generation history is only stored during the current session and is not saved to a file.

## Technologies Used

### Beginner

* Python
* random
* string

### Advanced

* Python
* Tkinter
* secrets
* string
* pyperclip

## Requirements

Python 3.12 or a compatible Python version is recommended.

The Advanced version also requires:

```text
pyperclip
```

Install it with:

```bash
pip install -r requirements.txt
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/daim-ul-hassan/OIBSIP.git
```

Go to the Task 3 folder:

```bash
cd Python-Task3-Random_Password_Generator
```

### Run the Beginner Version

```bash
python random-password-generator.py
```

### Run the Advanced Version

```bash
python advanced-random-password-generator.py
```

## How It Works

The user first chooses the desired password length and character types.

The program creates a character pool based on the selected options. The password is then generated from that pool.

The Advanced version uses Python's `secrets` module instead of `random` for password generation.

When character types are selected, the Advanced version also guarantees that at least one character from each selected type is included in the generated password.

## Advanced Password Strength

The Advanced version provides a simple strength indicator based on password length and character diversity.

The result is displayed as:

* Weak
* Medium
* Strong

The strength label also changes color based on the result.

## Ambiguous Characters

The Advanced version provides an option to exclude characters that can easily be confused with one another:

```text
0
O
l
1
```

When enabled, these characters are removed from the available character pools before the password is generated.

## Clipboard

The Advanced version uses `pyperclip` to copy generated passwords to the clipboard.

Passwords are automatically copied when generated. The user can also use the Copy to Clipboard button.

## Generation History

The Advanced version keeps the last 5 generated passwords during the current application session.

The history is stored in memory only. It is not written to a file or database.

## Project Structure

```text
Python-Task3-Random_Password_Generator/
│
├── random-password-generator.py
├── advanced-random-password-generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Task Checklist

### Beginner Tier

* [x] Password length with minimum of 8 characters
* [x] Uppercase letters
* [x] Lowercase letters
* [x] Numbers
* [x] Symbols
* [x] At least 2 character types
* [x] Password generation
* [x] Input validation
* [x] Generate another password without restarting

### Advanced Tier

* [x] GUI with password length control
* [x] Character type checkboxes
* [x] Secure generation using `secrets`
* [x] Password strength indicator
* [x] Character type requirements enforced
* [x] Copy to Clipboard
* [x] Automatic clipboard copying
* [x] Exclude ambiguous characters
* [x] Last 5 generated passwords in the current session

## OIBSIP

This project was completed as part of the Oasis Infobyte Internship Program Python Track.
