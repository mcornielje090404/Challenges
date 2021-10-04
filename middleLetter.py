##Function that returns the middle letter of a word if the word has 2 middle letters it returns blank space

repeat = True

def mid():
    word = input("What word would you like to use? ")
    test = len(word)
    middleLetter = word[len(word)//2]
    if test % 2 > 0:
        print(middleLetter)
    else:
        print("")

while repeat == True:
    mid()
