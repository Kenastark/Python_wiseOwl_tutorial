
import pandas as pd

# import 2 tables
films = pd.read_excel("/Users/ikenna/Documents/GitHub/Python/19 - Pandas/Films and directors.xlsx")

directors = pd.read_excel("/Users/ikenna/Documents/GitHub/Python/19 - Pandas/Films and directors.xlsx",sheet_name="Directors")

# join or combine these two tables
combined = pd.merge(films,directors,how="outer",left_on="DirectorId",right_on="DirectorId")
print(combined)


