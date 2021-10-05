def only_ints(input):
    try:
        val = int(input)
        print("Input is an integer")
    except ValueError:
        try:
            val = float(input)
            print("Input is a float")
        except ValueError:
            print("Input is a string")
while True:
    input1 = input("What is your value")
    only_ints(input1)
