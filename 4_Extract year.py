def extract_year(date_str:str) -> int
 """doct-string: Pull the year out of a date string.

    Assumes the year is the first four digits that appear, which holds for
    "2026-07-29", "2026/07/29" and "Joined on 2026-07-29" alike.

    Args:
        date_str: Any text containing a year, e.g. "2026-07-29".

    Returns:
        The year as an int, e.g. 2026.
    """
  digit_characters = ""
for character in date_str:
        if character.isdigit():
            digit_characters += character

  first_four_digits = digit_characters[:4]

    return int(first_four_digits)


if __name__ == "__main__":
    test_cases: list[tuple[str, int]] = [
        ("2026-07-29", 2026),
        ("1999-01-01", 1999),
        ("2020/12/31", 2020),
        ("2015-03-08 10:45", 2015),
        ("Joined on 2010-06-15", 2010),
    ]
    for date_text, expected_year in test_cases:
        actual_year = extract_year(date_text)
        result_label = "PASS" if actual_year == expected_year else "FAIL"
        print(f"[{result_label}] {date_text!r:<24} expected {expected_year}, got {actual_year}")
