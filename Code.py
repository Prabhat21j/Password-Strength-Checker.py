#
# Ps Number: 05
# Project Title: Password Strength Checker
# Student Name: Prabhat joshi
# Email: prabhat.joshi@rungta.org
# ERP No.: 01191
# Section: BCA 1-B
import re

def check_password(password):

    # Check empty password
    if password == "":
        print("Password cannot be empty.")
        return

    if re.search(r"\s", password):
        print("Password must not contain spaces.")
        return

    score = 0
    suggestions = []

    # Rule 1: Length must be at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("use at least 8 characters")

    # Rule 2: At least one uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("add an uppercase letter")

    # Rule 3: At least one lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("add a lowercase letter")

    # Rule 4: At least one digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("add a digit")

    # Rule 5: At least one allowed special character
    if re.search(r"[@#$%&*!]", password):
        score += 1
    else:
        suggestions.append("add a special character")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"Strength: {strength} ({score}/5)")

    # Display suggestions
    if suggestions:
        print("Suggestions: " + ", ".join(suggestions))
    else:
        print("No suggestions. Your password is secure.")


# Main program
password = input("Password: ")
check_password(password)
