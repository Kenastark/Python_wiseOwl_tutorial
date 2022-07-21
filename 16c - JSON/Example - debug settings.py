
import json

with open("/Users/ikenna/Documents/GitHub/Python/16c - JSON/launch.json") as settings_file:

    # load this into a variable
    settings = json.load(settings_file)

# test this
configurations = settings["configurations"]

print(type(configurations))
print(configurations)


real_config = configurations[0]
print(type(real_config))
print(real_config)

jmc = real_config["justMyCode"]
print(jmc)


