
if_just_letters = "(0800) 587 1456".isalpha()
print(if_just_letters)

# alphanumeric
if_just_letters_and_numbers = "08005871456".isalnum()
print(if_just_letters_and_numbers)

# does this start with 0800
if_starts_0800 = "(0800) 587 1456".startswith("(0800")
print(if_starts_0800)

# does it end with 6
if_ends_with_6  = "(0800) 587 1456".endswith("6")
print(if_ends_with_6)
