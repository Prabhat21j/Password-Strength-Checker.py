# 🔐 Password Strength Checker

## Project Details

- **University:** Rungta International Skills University
- **School:** School of Information Technology
- **Course:** Bachelor of Computer Application (BCA)
- **Student Name:** Prabhat Joshi
- **ERP ID:** 01191
- **Branch:** BCA 1B AIML
- **PS No.:** 5
- **Project Title:** Password Strength Checker
- **Language:** Python 3

## 📌 About Project

Password Strength Checker is a Python program that checks password security based on five rules. It classifies passwords as Weak, Medium, or Strong and provides suggestions to improve password strength.

## ⚙️ Features

- Checks minimum password length (8 characters).
- Checks uppercase letters.
- Checks lowercase letters.
- Checks digits.
- Checks special characters (@#$%&*!).
- Detects empty passwords.
- Rejects passwords containing spaces.
- Provides suggestions for weak passwords.

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (Regex)
- Strings
- Conditional Statements
- Lists
- Functions

## 📊 Password Classification

| Score | Strength |
|---|---|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

## ▶️ How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or terminal.
4. Run the following command:

```bash
python password_strength_checker.py
```

5. Enter your password.

## 🧪 Test Cases

| Password | Expected Result |
|---|---|
| abc123 | Weak (2/5) |
| Hello123 | Medium (4/5) |
| Empty | Invalid Input |
| Hello 123 | Invalid Input |
| Hello@123Xy | Strong (5/5) |

## 🎯 Objective

To understand password validation, regular expressions, conditional statements, and basic Python programming concepts.

## 📝 Conclusion

This project helps users understand password security and improve their passwords by identifying missing security requirements.

---

**Developed by: Prabhat Joshi**  
**ERP ID: 01191 | BCA 1B AIML**  
**Rungta International Skills University**
