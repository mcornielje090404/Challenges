## A code that can read a dictionary and return the amount of people online
statuses = {
    "Alice":"Online",
    "Bob":"Offline",
    "Eve":"Online",
    }

online = "Online"
amountOnline = 0
for key in statuses:
    if statuses[key] == online:
        amountOnline = amountOnline + 1

print("The amount of peeople online is ", str(amountOnline))
