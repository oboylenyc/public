""" Title: Extract Dates from Text

Difficulty: Intermediate

Challenge Description:
Write a function extract_dates(text: str) -> list[str] that finds all dates in a string using regular expressions.
For this challenge, support these formats:

DD/MM/YYYY

DD-MM-YYYY

YYYY/MM/DD

Constraints:

Day (DD) and month (MM) should always be two digits.

Year (YYYY) should be exactly four digits.

Return the list of matched dates in the order they appear """

import re
from datetime import date

# Matches: DD/MM/YYYY, DD-MM-YYYY, YYYY/MM/DD, YYYY-MM-DD
DATE_REGEX = re.compile(
    r"""
    (?:
        (?P<d1>\d{2})[/-](?P<m1>\d{2})[/-](?P<y1>\d{4})
    )
    |
    (?:
        (?P<y2>\d{4})[/-](?P<m2>\d{2})[/-](?P<d2>\d{2})
    )
    """,
    re.VERBOSE,
)

def extract_dates(text: str, *, validate: bool = False) -> list[str]:
    """Return dates found in `text` in the order they appear.
    Set validate=True to keep only real calendar dates."""
    found = []
    for m in DATE_REGEX.finditer(text):
        s = m.group(0)
        if validate:
            try:
                if m.group("d1") is not None:  # DD[-/]MM[-/]YYYY
                    d, mth, y = int(m.group("d1")), int(m.group("m1")), int(m.group("y1"))
                else:                           # YYYY[-/]MM[-/]DD
                    y, mth, d = int(m.group("y2")), int(m.group("m2")), int(m.group("d2"))
                date(y, mth, d)  # raises ValueError if invalid
            except ValueError:
                continue
        found.append(s)
    return found


# --- Quick tests ---
if __name__ == "__main__":
    txt = "Important dates: 05/09/2025, 2025-09-06, and 07-09-2025."
    print(extract_dates(txt))                     # ['05/09/2025', '2025-09-06', '07-09-2025']
    print(extract_dates("32/13/2025 2024/02/29", validate=True))  # ['2024/02/29']