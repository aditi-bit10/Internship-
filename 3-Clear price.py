def clean_price(text:str)-> float:
  """doc-string: turn messy price text into a number.
  
  Args:
        text: Raw price text such as "Rs. 499" or "1,299.00".

    Returns:
        The price as a float, or 0.0 if the text contains no digits at all.
  """
  has_a_digit = False
    for character in text:
        if character.isdigit():
            has_a_digit = True
    if not has_a_digit:
        return 0.0

kept_characters = ""
    for character in text:
        if character.isdigit() or character == ".":
            kept_characters += character

cleaned_text = kept_characters.strip(".")

 return float(cleaned_text)

if __name__ == "__main__":
    sample_prices = ["Rs. 499", "$12.50", "FREE", "1,299.00", ""]
    for sample in sample_prices:
        print(f"{sample!r:>12}  ->  {clean_price(sample)}")
