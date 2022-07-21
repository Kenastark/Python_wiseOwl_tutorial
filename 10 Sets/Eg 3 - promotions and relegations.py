
# read 2 files
with open("filePath") as pl1_file:
    pl1_teams = pl1_file.read().splitlines()

with open("filePath") as pl2_file:
    pl2_teams = pl2_file.read().splitlines()

# convert these lists to sets
pl1_set = set(pl1_teams)
pl2_set = set(pl2_teams)

# show the discrepancies
relegations = pl1_set - pl2_set
promotions = pl2_set - pl1_set

print("Relegations: " + repr(relegations))
print("Promotions: " +repr(promotions))





