import copy
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


# items = {
#     "Banana": "fruit",
#     "Apple": "fruit",
# }
# color = {
#         "blue" : "yes",
#         "yellow" : "no"
# }

# mixed = items | color

# print(mixed)

# ---------------------------------------

items = {
    "Banana": "fruit",
    "Apple": "fruit",
    "value":[10, 20]
}
# Shallow copy
# another_items = items.copy()

# deep 
more = copy.deepcopy(items)
more['value'].append(30)
print(items)
print(more)
# print(another_items)