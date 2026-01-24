# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "Blue" :"color"
# }

# print(items)
# -----------------------------

# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "blue" : "color"
# }

# key = input()
# if key in items:
#     print(items[key])
# else:
#     print("not found")

# ----------------------------------------------

# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "blue" : "color"
# }

# items.pop("blue")
# del items['Banana']

# print(items)


# ---------------
# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "blue" : "color"
# }

# print(len(items))
# print('Banana' in items)
# print(items)

# ----------------------------------
# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "blue" : "color"
# }

# for i in items:
#     print(i, items[i])

# -----------------------------------------------

# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
#     "color" : {
#         "blue" : "yes",
#         "yellow" : "no"
#     }
# }
# print(items['color']['blue'])
# print(len("color"))


items = {
    "Banana": "fruit",
    "Apple": "fruit",
}
color = {
        "blue" : "yes",
        "yellow" : "no"
}

mixed = items | color

print(mixed)