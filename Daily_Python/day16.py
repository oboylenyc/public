""" Title
Regex Email Extractor

Difficulty: Intermediate

Challenge Description:
Write a function that takes a block of text as input and extracts all valid email addresses using regular expressions.

A valid email has the format: username@domain.extension

Usernames may include letters, numbers, dots, underscores, or hyphens.

Domains may include letters, numbers, or hyphens.

Extensions should be 2–5 letters long.

Return a list of all matches in the order they appear. """

import re

# Compile once for reuse
EMAIL_RE = re.compile(
    r"\b[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,5}\b"
)

def extract_emails(text: str) -> list[str]:
    """
    Return all emails found in order of appearance.
    """
    return EMAIL_RE.findall(text)

# Bonus: unique emails (original case kept)
def unique_emails(text: str) -> set[str]:
    """
    Return a set of unique emails (order not guaranteed).
    """
    return set(extract_emails(text))


# --- quick test ---
if __name__ == "__main__":
    s = "Please contact us at support@example.com or sales@shop-now.org for more info."
    print(extract_emails(s))   # ['support@example.com', 'sales@shop-now.org']
    print(unique_emails(s))    # {'support@example.com', 'sales@shop-now_