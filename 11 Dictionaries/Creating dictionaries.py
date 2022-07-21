
# 1 - Setting up python
# 2 - Visual Studio Code
# 3 - Ranges, loops and formatting
# 4 - Virtual environments
# 5 - Modules

# method 1
vids = {
    1: "Set up",
    2: "VS Code",
    3: "Ranges, etc"
}

# loop over dictionary elements
for key, value in vids.items():

    print("{0} - {1}".format(key,value))

# doing it again
for video_number, video_title in vids.items():
    print(video_number,video_title)


# print(vids1)
# print(type(vids1))

# # method 2
# vids2 = dict(

#     V1 = "Set up",
#     V2 = "VC Code",
#     V3 = "Ranges, etc"
# )

# print(vids2)
# print(type(vids2))


