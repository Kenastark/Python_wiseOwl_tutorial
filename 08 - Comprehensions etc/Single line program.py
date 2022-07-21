
# List even squares as comma-delimited list:
# 4,16.36.64,....

print(",".join([str(x ** 2) for x in range(1,21) if x % 2 == 0]))





