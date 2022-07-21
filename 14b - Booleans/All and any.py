
# Checks for equality

annie = 2
neo = 2
marv = 1

tests = (
    annie == neo,
    annie > marv,
    marv > neo
)

# test if all true
all_true = all(tests)
print(all_true)

# test if ANY true
any_true = any(tests)
print(any_true)


