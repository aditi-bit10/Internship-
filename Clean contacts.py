def clean_contacts(filepath: str) -> list[tuple[str, str]]:
    """Read a messy contacts file and return only the usable entries.

    Args:
        filepath: Path to a file of "name,email" lines.

    Returns:
        A list of (name, email) tuples. Blank lines, "---" separators and
        lines with no "@" are skipped. Returns [] if the file is missing.
    """
    contacts: list[tuple[str, str]] = []

    try:
        with open(filepath, "r", encoding="utf-8") as contacts_file:
            all_lines = contacts_file.readlines()
    except FileNotFoundError:
        print(f"No file named {filepath} -- returning an empty list.")
        return []

    for line in all_lines:
        cleaned_line = line.strip()

        if not cleaned_line:            # blank line
            continue
        if cleaned_line.startswith("---"):   # separator line
            continue
        if "," not in cleaned_line:     # nothing to split on
            continue

        # Split ONCE, so anything after the first comma stays with the email.
        name_part, email_part = cleaned_line.split(",", 1)
        name = name_part.strip()
        email = email_part.strip()

        if "@" not in email:            # Meera's line lands here
            continue

        # "vikram@example.com extra" — keep the first whitespace-separated token.
        # Delete this line if you want to show the raw, still-messy email instead.
        email = email.split()[0]

        contacts.append((name, email))

    return contacts
