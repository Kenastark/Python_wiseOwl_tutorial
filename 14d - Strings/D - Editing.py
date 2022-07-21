
# transforming this:

#  "   Wise Owl Training Consultants   "

# to this:
# "Armadillo Trading"

from os import remove


original_text =  "   Wise Owl Training Consultants   "

# strip out the blanks(trimming)
revised_text = original_text.strip()

# remove the prefix and suffix
revised_text = revised_text.removeprefix("Wise ")
revised_text = revised_text.removesuffix(" Consultants")

# replace owl with Armadillo
revised_text = revised_text.replace("Owl", "Armadillo")

# Armadillo Training
# 123456789ABCDEFGHI

revised_text = revised_text[:13] + "d" + revised_text[15:]

print(revised_text)

