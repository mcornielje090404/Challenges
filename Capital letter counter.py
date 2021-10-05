
repeat = True
while repeat == True:
    string = input("Enter your string")
    capitals = set()
    for index, char in enumerate(string):
        if char == char.upper():
            capitals.add(index)
    print(capitals)
