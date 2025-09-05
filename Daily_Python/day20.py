""" Regex: Validating Strong Passwords

Difficulty: Intermediate

Challenge Description:
Write a function that checks if a password string is strong based on these rules:

At least 8 characters long

Contains at least one uppercase letter

Contains at least one lowercase letter

Contains at least one digit

Contains at least one special character (e.g., !@#$%^&*)

Return True if the password is strong, otherwise False. """

import re

def check_strong_password(password: str) -> list[str]:
    failed_rules = []

    if len(password) < 8:
        failed_rules.append("too short (min 8 chars)")
    if not re.search(r"[A-Z]", password):
        failed_rules.append("missing uppercase")
    if not re.search(r"[a-z]", password):
        failed_rules.append("missing lowercase")
    if not re.search(r"\d", password):
        failed_rules.append("missing digit")
    if not re.search(r"[!@#$%^&*]", password):
        failed_rules.append("missing special character")

    return failed_rules


# Examples
print(check_strong_password("Str0ng!Pass"))  
# Output: []

print(check_strong_password("weakpass"))  
# Output: ['missing uppercase', 'missing digit', 'missing special character']