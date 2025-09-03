""" Title
Regex Email Extractor

Difficulty: Intermediate

Challenge Description:
Write a function that takes a block of text as input and extracts all valid email addresses using regular expressions.

Assume valid emails follow the pattern: username@domain.extension.

The username can contain letters, numbers, dots, underscores, and hyphens.

The domain must contain only letters and numbers.

The extension is 2–4 letters long.
Return the list of emails found, in the order they appear. """

import re

# Compile once for reuse
EMAIL_RE = re.compile(
    r"""
    \b
    [A-Za-z0-9._%+-]+             # username: letters, digits, dots, underscores, %, +, -
    @
    (?:[A-Za-z0-9]                # domain label must start with letter/digit
       [A-Za-z0-9-]{0,61}         # middle: letters/digits/hyphens (up to 63 chars total per label)
       [A-Za-z0-9]                # must end with letter/digit
    )
    (?:\.[A-Za-z0-9]              # additional domain labels allowed
       [A-Za-z0-9-]{0,61}
       [A-Za-z0-9]
    )*
    \.[A-Za-z]{2,10}              # TLD: 2–10 letters
    \b
    """,
    re.VERBOSE | re.IGNORECASE,
)

def extract_emails(text: str) -> list[str]:
    """Return all emails found in order of appearance."""
    return EMAIL_RE.findall(text)

def unique_emails(text: str) -> set[str]:
    """Return a set of unique emails (order not guaranteed)."""
    return set(extract_emails(text))

# --- quick test ---
if __name__ == "__main__":
    s = """
    Valid: support@example.com, sales@shop-now.org, info@sub.domain.co.uk
    Invalid: -bad@domain.com, user@.com, test@domain-, user@@domain.com
    """
    print(extract_emails(s))
    print(unique_emails(s))
