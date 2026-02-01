# PASSWORD-CHECKER-
Password Checker 🔐 A simple password strength checker that validates security rules like length, symbols, numbers, and case sensitivity to help users create strong and secure passwords.
🔐 Password Checker (Python)
📌 Beginner-Friendly Description

This project is a Password Strength Checker built using Python.
It helps users create strong and secure passwords by checking basic security rules like minimum length, uppercase and lowercase letters, numbers, and special symbols.
The program also provides voice feedback using text-to-speech for better user interaction.

⚙️ Technical Description

This is a Python-based password validation system that evaluates password strength using rule-based logic.
It validates passwords against common security criteria such as length constraints, character diversity (uppercase, lowercase, digits, symbols), whitespace restrictions, and prevention of commonly used passwords.
The application integrates pyttsx3 for real-time voice feedback and uses system time to display contextual greetings.

✨ Features

Minimum password length validation (8 characters)

Checks for:

Uppercase letters

Lowercase letters

Digits

Special symbols

Blocks common and weak passwords

Rejects passwords with spaces

Text-to-speech feedback using pyttsx3

Time-based greeting system

🛠️ Technologies Used

Python

datetime module

time module

pyttsx3 (Text-to-Speech)

📂 Project Files

pass.py – Main password checker script 

pass

requirements.txt – Required Python libraries 

requriment

▶️ How to Run
pip install -r requirements.txt
python pass.py

🚀 Future Improvements

Password strength scoring system

GUI version using Tkinter

Password hashing

Support for more security rules
